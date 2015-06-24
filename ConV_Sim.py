from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# ffftfreq => gave corresponding freq from tx   
# fft => fourier transformation                                                                      
# abs => converted imaginary # to real # 
# fftshift => set zero at center

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
    FFTG = FFTG[1500:]
    return FFTG

# Creates Freq points for Freq Domain
def Freq_points(tx):
    a = np.fft.fftshift(np.fft.fftfreq(tx.size, tx[1] - tx[0]))
    a = a[1500:]
    return a

# Number of test points
N  = 3001         
                                                       
# X points for functions (tx => Time Domain; vx => Freq Domain)
tx = np.linspace(0, 2*np.pi, N)
vx = Freq_points(tx)

# T means the Fourier Transformed fucntion
# Create Signal f                                                                                                                 
f  = np.sin(2*np.pi*tx)   
Tf = Transform(f, 0)                                             
                                                             
# Create Signal g
g  = np.cos(2*np.pi*tx)
Tg= Transform(g, 0)

# Convolution of f o g & 
ConV = np.convolve(f, g,'full')

# Multiplying Transforms of f & g 
ConVT = Transform( Tf * Tg, 1 )

# Show that ConVT == T_ConV

plt.figure(5)
plt.plot(ConV, 'k', ConVT, 'g' )

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
plt. grid()
plt.show()




# Square Pulse 
"""
x = np.linspace(0.11,0.39,N)  
y = signal.square(2* np.pi*5*x)


plt.ylim(-2,2)
plt.plot(x,y,'b')
plt.title("Square Wave Pulse")

plt. grid()
plt.show()
"""
