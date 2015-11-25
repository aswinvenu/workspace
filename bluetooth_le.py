import pexpect 
import time
import sys

print "Program to establish a connection with Bluetooth LE and"
print "Store the data into a file"

print "======================================================="
if len(sys.argv) != 2:
    print "Error : must specify the bluetooth mac-addr or file_name"
    print "Usage : sudo python bluetooth_le.py <msc-addr> <file name>"
    sys.exit()

mac = sys.argv[1]
file_name = sys.argv[2]

f = open(file_name)

#running gatttools in background
gatt = pexpect.spawn("gatttool -I")


#Connecting to the device 
gatt.sendline("connect {0}".format(mac))
gatt.expect("Connection successful")

print "Press Ctrl+C to quit"

#Get the list of charactristics and UUIDs

print "list of characteristics and list of UUIDs"
gatt.sendline("primary")
    
print "Select the required UUID and characteristics of your device"

characteristics = raw_input("Enter the characteristics you ned to observe")

gatt.sendline("char-desc"+characteristics)

UUID = raw_input("Enter the UUID")

while True:

    gatt.sendline("char_read_uuid "+ characteristics +" "+ UUID + " " + UUID)
    string = gatt.before
    
    f.write(string)
    f.write("\n")

    time.sleep(0.08)


