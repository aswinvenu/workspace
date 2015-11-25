import serial

#change the port as per your setup. In this case my device is connected to
#/dev/rfcomm0. It will be the defualt one

reader = serial.Serial("/dev/rfcomm0",9600)

while(True):
    data = reader.readline().strip("/n/r")
    print data
    #need to write:
    #calculate the distance travelled 
    #plots
    #breath

