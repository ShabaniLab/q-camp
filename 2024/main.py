


import time
import pyvisa
import asyncio
from bleak import BleakClient
import numpy as np
###PID WEIGHTS###
pgain = 1
igain = 1
dgain = 1
###TUNE THESE#### please :)
# Define the UUIDs of the BLE service and characteristic
SERVICE_UUID = "12345678-1234-5678-1234-56789abcdef0"
CHARACTERISTIC_UUID = "12345678-1234-5678-1234-56789abcdef1"




def consolebrick(): # just for formatting #
    print('\n')
    a = '#'
    for i in range(5):
        print(a*30)
    print('\n')

def rotation_matrix_x(angle_degrees):
    angle_radians = np.radians(angle_degrees)
    return [
        [1, 0, 0],
        [0, np.cos(angle_radians), -np.sin(angle_radians)],
        [0, np.sin(angle_radians), np.cos(angle_radians)]
    ]

def rotation_matrix_y(angle_degrees):
    angle_radians = np.radians(angle_degrees)
    return [
        [np.cos(angle_radians), 0, np.sin(angle_radians)],
        [0, 1, 0],
        [-np.sin(angle_radians), 0, np.cos(angle_radians)]
    ]

def rotation_matrix_z(angle_degrees):
    angle_radians = np.radians(angle_degrees)
    return [
        [np.cos(angle_radians), -np.sin(angle_radians), 0],
        [np.sin(angle_radians), np.cos(angle_radians), 0],
        [0, 0, 1]
    ]

def rotate_vector(vector, adjustx, adjusty, adjustz):
    R_x = rotation_matrix_x(adjustx)
    R_y = rotation_matrix_y(adjusty)
    R_z = rotation_matrix_z(adjustz)

    # Sequentially apply the rotation matrices
    rotated_vector = np.dot(R_x, vector)
    rotated_vector = np.dot(R_y, rotated_vector)
    rotated_vector = np.dot(R_z, rotated_vector)

    return rotated_vector


#####POWER CONTROL#####
def VectorWrite(i,j,k,sec,devices): #floats < 1, only
    vector = [i,j,k]

    if sec:
        start = 3
    else:
        start = 0
    count = 0
    while count < 3:
        powersup(20,vector[count],devices[count+start])
        count+= 1
            #high v limit just incase, tune if it doesn't work. I can't do that without the supplies

def powersup(voltage, currentlim, device):
    if currentlim > 1:
        currentlim = 1
    if currentlim < -1:
        currentlim = -1
    if currentlim < .01 and currentlim > -.01:
        currentlim = .01
    raw = (
    ':SOUR:FUNC VOLT#'
    f':SOUR:VOLT {voltage}#'
    f':SOUR:VOLT:ILIM {currentlim}#'
    ':OUTP ON#'
    #':OUTP OFF'
    ).format(voltage=voltage, currentlim=currentlim, time=time)
#   print(raw)
    instructions = raw.split('#') # '#'s only serve as seperators
#    print(instructions)
    for i in instructions: # instructions string can be sent all at once with different formatting,
        device.write(i)    # this method helped with debugging/learning the commands. change if you
                           # deem it fit.
#####POWER CONTROL#####


#####CONTROL LOOP#####
class PIcontroller: ### look, I know the method/class name isn't updated.
    def __init__(self):
        self.errors = []
        print("init!")

    def PI(self, SP, PV):
        # Compute control output
        et = SP - PV
        self.errors.append(et)
        i = sum(self.errors)
        d = 0
        if len(self.errors) > 1:
            x = list(range(len(self.errors)))
            fd = [(self.errors[i + 1] - self.errors[i]) / (x[i + 1] - x[i]) for i in range(len(self.errors) - 1)]
            d = sum(fd) / len(fd)
            print(d)

        ut = pgain * et + igain * i + dgain * d
        npv = PV + ut

        return npv
#####CONTROL LOOP#####
xcon = PIcontroller() #init for each axis. One of these isn't needed
ycon = PIcontroller() #as gravity restrains the motion, but I won't know which it is until
zcon = PIcontroller() #I can test

#########################
##### MAIN FUNCTION #####
async def run(addresses):
    clients = [BleakClient(address) for address in addresses]
    try:
        # Connect to all devices
        await asyncio.gather(*[i.connect() for i in clients])

        # Function to read data from a single client
        async def read_data(client0,client1):
            try:
                consolebrick()

                rm = pyvisa.ResourceManager() # init Resource Manager
                print(rm.list_resources())
                g = 'TCPIP0::192.168.0.21::inst0::INSTR,TCPIP0::192.168.0.22::inst0::INSTR,TCPIP0::192.168.0.23::inst0::INSTR,TCPIP0::192.168.0.24::inst0::INSTR,TCPIP0::192.168.0.25::inst0::INSTR,TCPIP0::192.168.0.26::inst0::INSTR' # list all ports. Only select from the ones that aren't system default ("ASRL")
                g = g.split(",")
                print("available devices:")
                for i in g:
                    print(i + '\n')

                devices = []

                for i in g: #initialize each of the devices
                    devices.append(rm.open_resource(i))
                    print(i + "init!\n")
                VectorWrite(float(input("setpoint i: ")), float(input("setpoint j: ")), float(input("setpoint k: ")), False, devices)

                ax =1.0
                ay =1.0
                az =1.0
                ##### MAIN LOOP #####
                while True:
                    sensor1 = [0,0.0,0.0,0.0]
                    sensor2 = [0,0.0,0.0,0.0]

                    data = await client0.read_gatt_char(CHARACTERISTIC_UUID)
                    print(f"Received data from {client0.address}: {data.decode('utf-8')}")
                    data1 = await client1.read_gatt_char(CHARACTERISTIC_UUID)
                    print(f"Received data from {client1.address}: {data1.decode('utf-8')}")

                    data_str = data.decode('utf-8')
                    data_list = data_str.split(',')
                    data1_str = data1.decode('utf-8')
                    data1_list = data1_str.split(',')

                    sensor1 = data_list
                    sensor2 = data1_list

                    print(sensor1)
                    print(sensor2)

                    n = 0
                    while n < len(sensor1):
                        sensor1[n] = float(sensor1[n])
                        sensor2[n] = float(sensor2[n])
                        n+=1
                    adjustx = xcon.PI(sensor1[1],sensor2[1])
                    adjusty = ycon.PI(sensor1[2],sensor2[2])
                    adjustz = zcon.PI(sensor1[3],sensor2[3])
                    newv = rotate_vector([ax, ay, az], adjustx, adjusty, adjustz)
                    ax = newv[0]
                    ay = newv[1]
                    az = newv[2]
                    print('hi')
                    VectorWrite(ax,ay,az,True,devices) ### write updated values to second set of powersupplies

                    ### vec_update will be added to list of currents abd ->SHOULD<- directly respond.
                    ### in my dreams ...
                    await asyncio.sleep(.1)  # Read every .2 seconds, should probably decrease for more accurate pid
                ##### MAIN LOOP #####


            except Exception as e:
                print(f"Error: {e}")

        # Start reading data from each BLE device
        await asyncio.gather(*[read_data(clients[0],clients[1])])

    except Exception as e:
        print(f"Failed to connect or read data: {e}")

    finally:
        # Disconnect from all devices
        print("done!")
#####MAIN FUNCTION#####
#######################


#####CALL#####
def main():
    ## init vectors


    #####BLUETOOTH LE#####
    addresses = ['b9:e9:78:3f:10:da','9e:9d:53:fa:dc:16']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(addresses))

#####CALL#####


if __name__ == "__main__":
    main()
