import random
import pyaudio
import wave
import sys
import time 
import serial
import numpy as np

import threading 

serial_flag = True

locations = ["/dev/ttyACM0","/dev/ttyACM1","/dev/ttyACM2"]

for port in locations:
    try:
        
        print "Connecting to port:",port
        serial_port = serial.Serial(port,115200)
    except:
        print "Connecting to port:",port,"failed"

print "connected to port:",port 

def playback():

    global serial_flag

    CHUNK = 1024

    voice = ["one.wav","two.wav","three.wav","four.wav","five.wav","six.wav","seven.wav","eight.wav","nine.wav"]
    played_numbers = []
    rank = []
    dir_name = "/home/aswin/Downloads/"
    voice_enum = list(enumerate(voice, start=1))

# instantiate PyAudio (1)
    p = pyaudio.PyAudio()

    for i in range(0,10):
        
        rand_num = random.choice(voice_enum)
        rand_audio = rand_num[1]
        played_numbers.append(str(rand_num[0]))

        wf = wave.open(dir_name+rand_audio, 'rb')

# open stream (2)
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

# read data
        data = wf.readframes(CHUNK)

# play stream (3)
        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)

# stop stream (4)
        stream.stop_stream()
        stream.close()
    
        time.sleep(0.5)
        i+=1
    p.terminate()

    serial_flag = False
    
    print "Now your turn to enter the numbers"
    print "=================================="
    input_numbers = raw_input("Enter the numbers with spaces:")
    list_numbers = input_numbers.split(" ")
    
    while(len(list_numbers) < 10):
        list_numbers.append("N")

    print "Numbers displayed:",played_numbers
    print "Numbers you typed:",list_numbers
    for i in range(0,len(played_numbers)):
        if(played_numbers[i] == list_numbers[i]):
            rank.append(1)
        else:
            rank.append(0)
    success = (float(sum(rank))/float(len(played_numbers))*100)
    print rank
    print "Your percentage of success is = ", success,"%"

    # close PyAudio (5)

def isint(string):
    try:
        int(string)
        return True
    except:
        return False

def eeg_data(serial_port):
    
    file_dir = "/home/aswin/eeg_data/"
    file_name = "data_audio"+time.strftime("%Y_%m_%d_%H_%M")

    file_path = file_dir + file_name
    ofile = open(file_path,"w")
    
    while (serial_flag):
        
        string = serial_port.readline().strip("\0\n").split(",")
        if(isint(string[0]) and isint(string[1])):
            ofile.write(string[0]+"\n")

thread1 = threading.Thread(target=eeg_data, args=(serial_port,))
thread2 = threading.Thread(target=playback, args=())

    
thread1.start()
thread2.start()

