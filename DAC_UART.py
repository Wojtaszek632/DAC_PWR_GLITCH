import serial
import sys
import numpy as np

 
args = int(sys.argv[1])


ser = serial.Serial('COM6',115200,timeout=5) #'/dev/ttyUSB0'
ser.close()
ser.open()

strings = str(args) + '\n'
ser.write(bytes(strings,'UTF-8'))

ser.close()
    




