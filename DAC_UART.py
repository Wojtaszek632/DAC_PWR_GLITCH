import serial
import sys
import numpy as np

 
args = int(sys.argv[1])


ser = serial.Serial('COM6',115200,timeout=5) #'/dev/ttyUSB0'
ser.close()
ser.open()
print(args)
strings = str(args) + '\n'
print(strings)
ser.write(bytes(strings,'UTF-8'))
print(ser.readline())  # read a '\n' terminated line
print(ser.readline())  # read a '\n' terminated line
print(ser.readline())  # read a '\n' terminated line
print(ser.readline())  # read a '\n' terminated line

#ser.write(lowByte)
#print(ser.readline()) 

#print(ser.readline()) 
ser.close()
    




