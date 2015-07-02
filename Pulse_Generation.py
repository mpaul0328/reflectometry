import matplotlib.pyplot as plt
import numpy as np

# Number of test points
N  = 50        

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
def FFT_Graph(FFT):
    FFTG = np.fft.fftshift(abs(FFT))
    FFTG = FFTG[N/2:]
    return FFTG

# Creates Freq points for Freq Domain
def Freq_points(tx):
    a = np.fft.fftshift(np.fft.fftfreq(tx.size, tx[1] - tx[0]))
    a = a[N/2:]
    return a

# Pulse Generator(Pulse @ bin 20)
tx = np.linspace(0,30*np.pi, N)
vx = Freq_points(tx)

y = np.zeros(N)
y[20] = 1

# FFT of Pulse -> Constant line across all vx
Ty = Transform(y, 0)


TyG = FFT_Graph(Ty)

plt.figure(1)
plt.plot(vx, TyG,'g')
plt.xlabel('Frequency')
plt.title('Frequency Domain')

plt.figure(2)
plt.plot(tx,y,'b')
plt.xlabel('Time')
plt.title("Time Domain")

plt.grid()
plt.show()
