'''run bpcalibra.py ant_0 ant_1 ant_2 ... ant_7
    
    Takes 8 ROACH ADC Samples, combines them, and plots the signal
inputs of the ROACH.'''

from sys import argv as arg
import matplotlib.pyplot as plt, numpy as np

# Open all NPZ files and data arrays
ant0 = np.load(arg[1])['data']
ant1 = np.load(arg[2])['data']
ant2 = np.load(arg[3])['data']
ant3 = np.load(arg[4])['data']
ant4 = np.load(arg[5])['data']
ant5 = np.load(arg[6])['data']
ant6 = np.load(arg[7])['data']
ant7 = np.load(arg[8])['data']
# Combine all ADC Samples
data = np.hstack((ant0, ant1, ant2, ant3, ant4, ant5, ant6, ant7)).flatten()
vdata = np.fft.fft(data) 
t = np.linspace(0,30*np.pi, len(data)) # x-axis of Time Domain
v = np.fft.fftshift(np.fft.fftfreq(t.size, t[1] - t[0])) # x-axis of Frequency Domain

plt.figure(6)
plt.plot(data, 'r')

plt.figure(5)
plt.plot(v, np.fft.fftshift(vdata.real), v, np.fft.fftshift(vdata.imag))
plt.plot(v, np.fft.fftshift(np.abs(vdata)), 'r')

plt.show()