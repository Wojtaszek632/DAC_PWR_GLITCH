import serial
import sys
import numpy as np

 
args = int(sys.argv[1])


ser = serial.Serial('COM6',115200,timeout=5) #'/dev/ttyUSB0'
ser.close()
ser.open()

if ( args <= 330 ) and ( args >= 0 ):
    strings = str(args) + '\n'
    ser.write(bytes(strings,'UTF-8'))

ser.close()
    




