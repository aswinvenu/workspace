import serial
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.fftpack import fft, fftfreq, fftshift
from scipy import ifft 
from scipy.signal import firwin
from scipy.signal import lfilter
from drawnow import *

locations = ['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2']

def band_pass(highcut,lowcut):
    nyq = 125
    high = highcut/nyq
    low = lowcut/nyq
    fir_coeff = firwin(100, [high, low], pass_zero = False,window='hanning')
    return fir_coeff

def bandpass_filter(data, highcut, lowcut):
    fil_coeff= band_pass(highcut,lowcut)
    y = lfilter(fil_coeff, 1.0, data)
    return y

def isint(s):
    try:
        int(s)
        return True
    except:
        return False

def filterplot():

    plt.title("Filtered EEG signal")
    plt.plot(old_filter,color='r')
    plt.xlabel("Time ----------->")
    plt.ylabel("Amplitude------------>")
    plt.grid()
    plt.xlim(0,999)
    #plt.ylim(-20000,20000)
    plt.draw()

for device in locations: 
    try:
        print "Trying....",device 
        arduino = serial.Serial(device,115200)
        break
    
    except:
        print "Failed to connect Device",device 

print "You are connected!"

channel1_data = [] 
old_filter = []
old_filer_data = []
low_cut = 30.0
high_cut = 3.0
fs = 250

while(len(channel1_data) <= 1000):

    while(arduino.inWaiting() == 0):
        pass
    data_string = arduino.readline()
    if(isint(data_string)):
        channel1_data.append(int(data_string))
    else:
        pass

fil_data = bandpass_filter(channel1_data, high_cut, low_cut) 
old_filter = fil_data.tolist()
drawnow(filterplot)

while(True):
    i = 0
    if(len(channel1_data) >= 1000):
       while i<200:
            
            channel1_data.pop(0)
            old_filter.pop(0)
            i += 1

    while(len(channel1_data) <= 1000):

        data_string = arduino.readline()
        #parsed_data = data_string.split(" ")
        if (isint(data_string)):
            channel1_data.append(int(data_string))
        else:
            pass

    fil_data = bandpass_filter(channel1_data, high_cut, low_cut)
    filter_data = fil_data.tolist()
    old_filter = old_filter + filter_data[800:]
    drawnow(filterplot)

    plt.pause(0.00001)
        
            
