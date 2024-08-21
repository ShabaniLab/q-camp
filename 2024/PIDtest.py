###libs###
import matplotlib.pyplot as pyplot
import time
import random
import numpy as np
import pyvisa
import bluetooth

###values###
pgain = 1
igain = 1
dgain = .2

class PIcontroller:
    def __init__(self):
        self.errors = []
    def PI(self,SP,PV):
        ###error + proportion###
        et = SP - PV
        self.errors.append(et)
        ###integral###
        i = sum(self.errors)
        d = 0
        if len(self.errors) > 1:
            x = list(range(len(self.errors)))
            fd = [(self.errors[i + 1] - self.errors[i]) / (x[i + 1] - x[i]) for i in range(len(self.errors) - 1)] 
            d = sum(fd)/len(fd)
            print(d)

        ut = pgain*et + igain*i + dgain*d
        npv = PV + ut

        return(npv)


def PIDTEST()
    theta0 =float(input("INIT THETA0: "))
    phi0 =float(input("INIT PHI0: "))

    theta1 =float(input("INIT THETA1: "))
    phi1 =float(input("INIT PHI1: "))

    contheta = PIcontroller()
    conphi = PIcontroller()

    while(True):
        print("P0: " + str(phi0) + " P1: " + str(phi1) + " DIFF: " + str(abs(phi1-phi0)))
        phi1 = conphi.PI(phi0, phi1) # PI, phi0 is set, phi1 is proccessvar
        phi0 = phi0 + (random.random() - .5 )*phi0*.10 #simulate noise, max 5% jerk

        print("T0: " + str(theta0) + " T1: " + str(theta1) + " DIFF: " + str(abs(theta1-theta0)))
        theta1 = contheta.PI(theta0, theta1) 
        theta0 = theta0 + (random.random() - .5 )*theta0*.10 
        time.sleep(1)
 

    
