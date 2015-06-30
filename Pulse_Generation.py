from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
from sympy import functions

def Delta(x):
    return functions.special.delta_functions.DiracDelta(x) 

# Number of Test Points
N = 5

x = [2,3,4,5,6,7,8]


plt.figure(4)
plt.plot(Delta(x))
plt.grid()
plt.show()

"""
y = np.zeros(N)
i = N/2
y[i-3:i+2] = 0.15, 0.3, 0.5, 0.3, 0.15

yf = np.fft.fft(y)
xf = np.fft.fftfreq(x.size, x[1] - x[0])

plt.figure(1)
plt.plot(np.fft.fftshift(abs(xf)), np.fft.fftshift(np.abs(yf)),'g')
plt.xlabel('Frequency')
plt.title('Frequency Domain')

plt.figure(2)
plt.plot(x,y,'b')
plt.xlabel('Time')
plt.title("Time Domain")

plt.grid()
plt.show()
"""