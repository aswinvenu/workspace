from scipy.signal import spectrogram,hanning
import sys
from matplotlib.pyplot import *

file_name = sys.argv[1]

f = file(file_name,'r')
fs = 250

channel1_data = []
channel2_data = []

for i in range(0,75000):
    
    data_string = f.readline().split('\t')   
    channel1_data.append(float(data_string[0]))
    channel2_data.append(float(data_string[1]))
subplot(1,2,1)
Pxx1,freq1,bins1, im1 = specgram(channel1_data,NFFT = 1024, Fs=fs)
subplot(1,2,2)
Pxx2,freq2,bins2, im2 = specgram(channel2_data,NFFT = 1024, Fs=fs)
show()
