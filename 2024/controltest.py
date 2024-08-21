import pyvisa # only run this after you are plugged into the power supplies ... NI-VISA and pyvisa install required, ask Alex
import time 
import bluetooth 
import json

#sensor_1 = '' # we have to find these # I have no way of knowing this works untill we get the chips
#sensor_2 = '' # same goes for all bluetooth/sensor code 
#socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#socket.connect((sensor_address, 1))
#socket.connect((sensor_address, 2))


def consolebrick(): # just for formatting
    print('\n')
    a = '#'
    for i in range(5):
        print(a*30)
    print('\n')

consolebrick()

rm = pyvisa.ResourceManager() # init Resource Manager
g = rm.list_resources() # list all ports. Only select from the ones that aren't system default ("ASRL")

print("available devices:")
for i in g:
    print(i + '\n')

addrs = [] #ports for initializing devices

print('pick n \n') # pick how many power supplies you want
numadd = input('n:\n') # 1 sphere  -> 3, # 2 sphere -> 6

print('pick list index(s) (see device list): \n') # manually add addresses (0 index)
for i in range(int(numadd)):
    addrs.append(g[int(input("index:\n"))])

consolebrick()

print("addresses selected:\n")
devices = []

for i in addrs: #initialize each of the devices from the stored ports, add it to devices list
    print(i)
    devices.append(rm.open_resource(i))

consolebrick()

#ts finna get messy

def powersup(voltage, currentlim, device):
    raw = ('*RST#'
    ':SOUR:FUNC VOLT#'
    f':SOUR:VOLT {voltage}#'
    f':SOUR:VOLT:ILIM {currentlim}#'
    f':TRIG:LOAD "SimpleLoop", 1, 1#'
    ':OUTP ON#'
    ':INIT#'
    '*WAI#'
    #':OUTP OFF'
    ).format(voltage=voltage, currentlim=currentlim, time=time)
#   print(raw)
    instructions = raw.split('#') # '#'s only serve as seperators 
#    print(instructions)
    for i in instructions: # instructions string can be sent all at once with different formatting,
        device.write(i)    # this method helped with debugging/learning the commands. change if you
                           # deem it fit.

def VectorWrite(i,j,k): #floats < 1, only
    if len(devices) != 3:
        print('\nWarning! Incorrect number of supplies!\n')
    else:
        vector = [i,j,k]
        count = 0
        while count < 4:
            powersup(20,vector[count],devices[count]) #high v limit just incase, tune if it doesn't work. I can't do that without the supplies

def updatesupply(): #recursively """update""" the """"""CLI"""""""
    consolebrick()
    x = int(input("1. Turn off a supply\n2. Configure a supply\n3. Vector input\n4. Manual SCPI send\n"))
    if x == 1: # this should probably be a switch 
        command = int(input("device index:\n"))
        devices[command].write(':OUTP OFF')
        updatesupply()
    if x == 2:
        d = int(input("device index: "))
        v = float(input("voltage: "))
        i = float(input("current: "))
        powersup(v,i,d)
        updatesupply()
    if x == 3:
        i = float(input("i: "))
        j = float(input("j: "))
        k = float(input("k: "))
        VectorWrite(i,j,k)
        updatesupply()
    if x == 4:
        query = bool(input("query?: "))
        message = input("command: ")
        ind = input("device index: ")
        if query:
            device[ind].query(message)
        else:
            device[ind].write(message)
        updatesupply()

updatesupply()


#while True: #I [did] entirely redo this segment to work with vectors, and change current vs voltage
 #   x = input("update: [exit,deviceindex,voltage]")
  #  parsed = x.split(",")
   # if int(parsed[0]) == 1:
    #    devices[int(parsed[1])].write(':OUTP OFF')
     #else:
        #powersup(float(parsed[2]),1,devices[int(parsed[1])])

            #for those unfortunate enough to work with my code:
            #When testing the update, follow to format:

            #   exit?[INT],device number[INT],voltage[FLOAT]

            #Do not skip exit?, if you want it to stay on, just put something else

                
