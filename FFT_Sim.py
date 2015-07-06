import matplotlib.pyplot as plt
import numpy as np

# Number of Test Points
N = 5000

# Points taken between interval on x- axis
x = np.linspace(0.0, 2*np.pi, N)
# Signal(y-function)
y = np.cos(2*np.pi*80*x) + np.sin(2*np.pi*50*x)

# Fourier Transformation of signal
yf = np.fft.fft(y)
# Frequency Bins
xf = np.fft.fftfreq(x.size, x[1] - x[0])

plt.figure(1)
# Shifted to make zero the center; only taking positive frequencies; making imaginary, real 
plt.plot(np.fft.fftshift(abs(xf)), np.fft.fftshift(np.abs(yf)),'g')
plt.xlabel('Frequency')
plt.title('Frequency Domain')

plt.figure(2)
plt.plot(x,y,'b')
plt.xlabel('Time')
plt.title("Time Domain")

plt.grid()
plt.show()