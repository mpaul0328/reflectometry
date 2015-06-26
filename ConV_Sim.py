from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# fftfreq => gave corresponding freq from tx   
# fft => fourier transformation                                                                      
# abs => converted imaginary # to real # 
# fftshift => set zero at center

# Number of test points
N  = 5000        

# Fourier Transform of Signal
# Select 1 for Inverse FFFT
def Transform(signal, inverse):
    if inverse == 1:
        IFFT = np.fft.ifft(signal)
        return IFFT
    else:
        FFT = np.fft.fft(signal)
        return FFT

# Converts FFT for Graphing 
def FFT_Graph(FFT):
    FFTG = np.fft.fftshift(abs(FFT))
    FFTG = FFTG[N/2:]
    return FFTG

# Creates Freq points for Freq Domain
def Freq_points(tx):
    a = np.fft.fftshift(np.fft.fftfreq(tx.size, tx[1] - tx[0]))
    a = a[N/2:]
    return a


# Fourier Transforms (FFT)                                         
# X points for functions (tx => Time Domain; vx => Freq Domain)
tx = np.linspace(0, 2*np.pi, N)
vx = Freq_points(tx)

# First & Last 50 points (zeros)
zero_out = np.zeros(N)
zero_out[N/4 : (3*N)/4] = 1

# T means the Fourier Transformed fucntion
# Create Signal f                                                                                                                 
f  = np.sin(2*np.pi*tx)   
f *= zero_out
Tf = Transform(f, 0)                                             
                                                             
# Create Signal g
g  = np.cos(2*np.pi*tx)
g *= zero_out
Tg= Transform(g, 0)


# Convolution THM [f o g] & FFTs
# Proof: T{f o g} = Tf * Tg
# {f o g}
ConV = np.convolve(f, g,'same') 

# T{f o g}
TConV = Transform(ConV, 0)

# Tf * Tg
MT = Tf * Tg

# Remove Multi-Line comment to show Proof of Equivalence
"""
MTG = FFT_Graph(MT)
TConVG = FFT_Graph(TConV)
plt.figure(5)
plt.plot(vx, MTG, 'r', vx, TConVG, 'y')
"""

# Proof: {f o g} = T^-1{Tf * Tg}
# T^-1{Tf * Tg}
ITMT = Transform(MT, 1)

# Remove Multi-Line comment to show Proof of Equivalence
"""
plt.figure(6)
plt.plot(tx, ConV, 'r', tx, np.fft.fftshift(ITMT), 'b' )
"""

# Remove Multi-Line comment to show graphs of Time & Freq of f & g
"""
TgG = FFT_Graph(Tg)
TfG = FFT_Graph(Tf)  

plt.figure(1)
plt.plot(vx, TfG,'k')
plt.title('Frequency Domain of F')
plt.xlabel('Frequency')

plt.figure(2)
plt.plot(tx,f,'k')
plt.title('Time Domain of F')
plt.xlabel('Time')

plt.figure(3)
plt.plot(vx, TgG,'b')
plt.title('Frequency Domain of G')
plt.xlabel('Frequency')

plt.figure(4)
plt.plot(tx,g,'b')
plt.title('Time Domain of G')
plt.xlabel('Time')
"""
plt.grid()
plt.show()
