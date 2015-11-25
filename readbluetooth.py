import serial

reader = serial.Serial("/dev/rfcomm0",9600)

while(True):
    data = reader.readline().strip("/n/r")
    print data
