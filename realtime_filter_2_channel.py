import serial
import time
import sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.fftpack import fft, fftfreq, fftshift
from scipy import ifft 
from scipy.signal import firwin
from scipy.signal import lfilter
from drawnow import *

matplotlib.use("TkAgg")
locations = ['/dev/ttyACM0','/dev/ttyACM1','/dev/ttyACM2']

def band_pass(highcut,lowcut):
    nyq = 125
    high = highcut/nyq
    low = lowcut/nyq
    fir_coeff = firwin(125, [high, low], pass_zero = False,window='hanning')
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

    plt.subplot(1,2,1)
    plt.title("Filtered EEG signal from channel1")
    plt.plot(old_filter1,color='r')
    plt.xlabel("Time ----------->")
    plt.ylabel("Amplitude------------>")
    plt.grid()
    plt.xlim(0,999)
    #plt.ylim(-1000000,1000000)
    plt.subplot(1,2,2)
    plt.title("Filtered EEG Signal from channel 2")
    plt.plot(old_filter2,color='b')
    plt.xlabel("Time--------->")
    plt.ylabel("Amplitude----->")
    plt.grid()
    plt.xlim(0,999)
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
channel2_data = []
old_filter1 = []
old_filter2 = []
old_filer_data1 = []
old_filter_data2 = []
low_cut = 30.0
high_cut = 3.0
fs = 250

while(len(channel1_data) <= 1000):

    while(arduino.inWaiting() == 0):
        pass
    data_string = arduino.readline().split(",")
    if len(data_string)>=2 :

        if((isint(data_string[0])) and (isint(data_string[1]))):
            channel1_data.append(int(data_string[0]))
            channel2_data.append(int(data_string[1]))
        else:
            pass

fil_data1 = bandpass_filter(channel1_data, high_cut, low_cut)
fil_data2 = bandpass_filter(channel2_data, high_cut, low_cut)
old_filter1 = fil_data1.tolist()
old_filter2 = fil_data2.tolist()
drawnow(filterplot)

while(True):
    i = 0
    if(len(channel1_data) >= 1000):
       while i<200:
            
            channel1_data.pop(0)
            old_filter1.pop(0)
            channel2_data.pop(0)
            old_filter2.pop(0)
            i += 1

    while(len(channel1_data) <= 1000):

        data_string = arduino.readline().split(",")
        #parsed_data = data_string.split(" ")
        if ((isint(data_string[0])) and (isint(data_string[1]))):
            channel1_data.append(int(data_string[0]))
            channel2_data.append(int(data_string[1]))
        else:
            pass

    fil_data1 = bandpass_filter(channel1_data, high_cut, low_cut)
    fil_data2 = bandpass_filter(channel2_data, high_cut, low_cut)
    filter_data1 = fil_data1.tolist()
    filter_data2 = fil_data2.tolist()
    old_filter1 = old_filter1 + filter_data1[800:]
    old_filter2 = old_filter2 + filter_data2[800:]

    drawnow(filterplot)

    plt.pause(0.00001)
        
            
