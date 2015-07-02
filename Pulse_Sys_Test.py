import matplotlib.pyplot as plt
import numpy as np

# Number of test points
N  = 50  

# SYSTEM UNDER TEST (DO NOT KNOW) Use any # to argue
def Tri(x):
    sY = np.array(range(0,50))
    sY[25:] = sY[24::-1]
    sY[16:35] = 15
    return sY

# Fourier Transform of Signal
# Select 1 for Inverse FFT
def Transform(signal, inverse):
    if inverse == 1:
        IFFT = np.fft.ifft(signal)
        return IFFT
    else:
        FFT = np.fft.fft(signal)
        return FFT

# Converts FFT for Graphing 
# Only Use 1 for 
def FFT_Graph(FFT):
    FFTG = np.fft.fftshift(abs(FFT))
   # if x == 1:
      #  FFTG = FFTG[N/2:]
    return FFTG

# Creates Freq points for Freq Domain
def Freq_points(tx):
    a = np.fft.fftshift(np.fft.fftfreq(tx.size, tx[1] - tx[0]))
    #a = a[N/2:]
    return a


tx = np.linspace(0,30*np.pi, N)
vx = Freq_points(tx)

"""
--------------Pulse Generation---------------
"""
# Pulse Generator(Pulse @ bin 0)
p = np.zeros(N)
p[20] = 1

# FFT of Pulse -> Constant line across all vx
Tp = Transform(p, 0)

"""
--------------TESTING SYSTEM----------------
"""
# Tri(1) is in frequency domain and is assumed Transformed
Ts = Tri(1)

# Pulse is sent into system and gets multiplied
# Convolution THM T{p o s} = Tp * Ts
out = Tp * Ts

"""
------------------ANALYSIS------------------
"""
# Take out and Inverse Transform it to produce the convolution of p o s
# ITout is in time domain
ITout = Transform(out, 1)
Slice = ITout[20:]  
Part = ITout[:20]

# New output in time domain w/ pulse moved
Output = np.zeros(N)
Output[:30] = Slice
Output[30:] = Part

Sys_Int = Transform(Output, 0)


# All Graphs in order of action (Each Graph has Description)

plt.figure(6)
plt.plot(p, 'r')
plt.title('Pulse in Time Doamin Before Test')

TpG = FFT_Graph(Tp)
plt.figure(5)
plt.plot(vx,TpG, 'r')
plt.title('Pulse in Frequency Domain Before Test')

outG = FFT_Graph(out)
plt.figure(4)
plt.plot(vx, outG, 'b')
plt.title("Pulse multiplied w/ System in Frequency Domain (Output)")

plt.figure(3)
plt.plot(ITout, 'g')
plt.title('Inverse Transform of output which gives Convolution of Pulse & System')

plt.figure(2)
plt.plot(Output, 'y')

Sys_IntG = FFT_Graph(Sys_Int)
plt.figure(1)
plt.plot(Sys_IntG, 'm')

plt.figure(1)
plt.plot(Tri(1), 'k')

plt.grid()
plt.show()