from scipy.signal import spectrogram,hanning
import sys
from matplotlib.pyplot import *

file_name = sys.argv[1]

f = file(file_name,'r')
fs = 250

channel1_data = []

for i in range(0,6250):
    
    data_string = f.readline().strip("\n")
    channel1_data.append(float(data_string))
Pxx1,freq1,bins1, im1 = specgram(channel1_data,NFFT = 1024, Fs=fs)
show()
