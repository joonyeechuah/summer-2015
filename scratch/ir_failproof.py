#!/usr/bin/env python

import time
from BrickPi import *   								

TIMEOUT = 30
BAD_RESPONSE = 1000

BrickPiSetup()
BrickPi.SensorType[PORT_1] = TYPE_SENSOR_EV3_INFRARED_M0
BrickPiSetupSensors()

def Read_IR_Distance( port, default):
    response = BAD_RESPONSE
    t1 = time.time()
    t2 = t1
    while (( t2 - t1 ) <= 30 ) & ( response >= BAD_RESPONSE ):
        result = BrickPiUpdateValues()
        if not result:
            response = BrickPi.Sensor[port]
            t2 = time.time()
            elapsed = t2 - t1
            if (response < BAD_RESPONSE):
                print "Elapsed\t" + str(elapsed) + "\tValue\t" + str(response)
                return response
            time.sleep(0.01)

    print "Failed\t" + str(TIMEOUT) + "\tValue\t" + str(default)
    return default

while True:
    infrared = Read_IR_Distance( PORT_1, 0 )
    #print str(infrared)

