import time
import sys
import numpy as np
import matplotlib
import matplotlib.pylab as plt
import matplotlib.animation as animation
from scipy.fftpack import fft, fftfreq, fftshift
from scipy import ifft 
from scipy.signal import firwin
from scipy.signal import lfilter
from drawnow import *
matplotlib.use("TkAgg")

file_name = sys.argv[1]
f = file(file_name,'r')

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

channel1_data = []
filter1_data = []
fft1_data = []
low_cut = 40.0
high_cut = 1.0
fs = 250

for i in range(0,2500):
    data_string = f.readline().strip('\n\0')
    channel1_data.append(float(data_string))
    

filter1_data = bandpass_filter(channel1_data, high_cut, low_cut)
fft1_data = np.abs(fft(filter1_data,250))
fft1_data = fft1_data[0:50]
t = np.arange(0,10,0.004)

plt.subplot(2,2,1)
plt.title("EEG data from Hiren")
plt.plot(t,channel1_data)
plt.grid()
plt.subplot(2,2,2)
plt.title("EEG filtered signal")
plt.plot(t,filter1_data)
plt.grid()
plt.subplot(2,2,3)
plt.plot(fft1_data)
plt.grid()
plt.subplot(2,2,4)
Pxx,freq,bins,im = plt.specgram(filter1_data,NFFT=250,Fs=fs)
plt.show()

            
