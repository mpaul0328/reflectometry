import matplotlib.pyplot as plt, numpy as np

N  = 500 # Number of test points
PLS = 20 # pulse location

def bandpass(x):
    '''SYSTEM UNDER TEST (DO NOT KNOW) Use any # to argue'''
    bp = np.arange(N)
    bp[N/2:] = bp[N/2-1::-1]
    bp[16:-15] = 15
    return bp

def fft_graph(data):
    '''Converts FFT data for Graphing'''
    return np.fft.fftshift(np.abs(data))

t = np.linspace(0,30*np.pi, N)
v = np.fft.fftshift(np.fft.fftfreq(t.size, t[1] - t[0]))

p = np.zeros(N); p[PLS] = 1 # Pulse Generator(Pulse @ bin 0)
vp = np.fft.fft(p) # FFT of Pulse -> Constant line across all v
vs = bandpass(1) # bandpass(1) is in frequency domain and is assumed np.fft.ffted
vps = vp * vs # Pulse is sent into system and gets multiplied, Convolution THM T{p o s} = vp * vs

# Take vps and Inverse np.fft.fft it to produce the convolution of p o s
# ps is in time domain
ps = np.fft.ifft(vps)
ps_d = np.concatenate([ps[PLS:],ps[:PLS]])
bp = np.fft.fft(ps_d) # New vpsput in time domain w/ pulse moved

# All Graphs in order of action (Each Graph has Description)
plt.figure(6)
plt.plot(p, 'r')
plt.title('Pulse in Time Domain Before Test')

plt.figure(5)
plt.plot(v, vp.real, v, vp.imag)
plt.plot(v, fft_graph(vp), 'r')
plt.title('Pulse in Frequency Domain Before Test')

plt.figure(4)
plt.plot(v, fft_graph(vps), 'b')
plt.title("Pulse multiplied w/ System in Frequency Domain (ps_d)")

plt.figure(3)
plt.plot(ps, 'g')
plt.title('Inverse np.fft.fft of vpsput which gives Convolution of Pulse & System')

plt.figure(2)
plt.plot(ps_d, 'y')

plt.figure(1)
#plt.plot(fft_graph(bp), 'm')
plt.plot(bp, 'm')
plt.plot(bandpass(1), 'k')

plt.show()
