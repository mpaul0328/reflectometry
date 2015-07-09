import matplotlib.pyplot as plt, numpy as np

N  = 500 # Number of test points
PLS = 20 # pulse location

def bandpass(x):
    '''SYSTEM UNDER TEST (DO NOT KNOW) Use any # to argue'''
    return np.sin(49*t) + np.sin(69*t)

t = np.linspace(0,30*np.pi, N) # x-axis of Time Domain
v = np.fft.fftshift(np.fft.fftfreq(t.size, t[1] - t[0])) # x-axis of Frequency Domain
p = np.zeros(N); p[PLS] = 1 # Pulse Generator(Pulse @ bin 20)
vp = np.fft.fft(p) 
vs = bandpass(1) # bandpass(1) is in frequency domain and is assumed Fourier Transformed
vps = vp * vs # Pulse is sent into system and gets multiplied, Convolution THM T{p o s} = vp * vs
ps = np.fft.ifft(vps) # Take vps and Inverse Fourier Transform it to produce the convolution of p o s 
ps_d = np.concatenate([ps[PLS:],ps[:PLS]]) # Deconvolve ps; ps is in time domain
bp = np.fft.fft(ps_d) # Bandpass derived from Convolution THM

# Remove Multi-Line comment to show graphs
"""
plt.figure(6)
plt.plot(p, 'r')
plt.title('Pulse in Time Domain Before Test')

plt.figure(5)
plt.plot(v, vp.real, v, vp.imag)
plt.plot(v, np.fft.fftshift(np.abs(vp)), 'r')
plt.title('Pulse in Frequency Domain Before Test')

plt.figure(4)
plt.plot(v, np.fft.fftshift(np.abs(vps)), 'k')
plt.plot(v, vps.real, v, vps.imag)
plt.title("Pulse multiplied w/ System in Frequency Domain ")

plt.figure(3)
plt.plot(t, ps, 'g')
plt.title('Inverse Fourier Transofrm of vps which gives Convolution of Pulse & System')

plt.figure(2)
plt.plot(t, ps_d, 'c')
plt.title('Deconvolving: Sliding pulse back')

plt.figure(1)
plt.plot(v, bp, 'm')
plt.plot(v, bandpass(1), 'k')
plt.title('The System Interference in Frequency Domain')

plt.show()
"""