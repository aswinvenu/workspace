import random
import pyaudio
import wave
import sys
import time 
import serial
import numpy as np
from scipy.signal import firwin
from scipy.signal import lfilter 

import csv
import threading 

CHUNK = 1024

voice = ["one.wav","two.wav","three.wav","four.wav","five.wav","six.wav","seven.wav","eight.wav","nine.wav"]

voice_enum = list(enumerate(voice, start=1))

dir_name = "/home/aswin/Downloads/"


# instantiate PyAudio (1)
p = pyaudio.PyAudio()

played_numbers = []

for i in range(0,10):
    
    rand_num = random.choice(voice_enum)
    rand_audio = rand_num[1]
    played_numbers.append(rand_num[0])

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
    
    # close PyAudio (5)
p.terminate()
print played_numbers
