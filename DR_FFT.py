import matplotlib.pyplot as plt    # import all the files necessary for our algorithm 
import numpy as np     # to work by taking the Fast Fourier Transform 

                       # of a sin function

x = np.linspace(0.0, 2*np.pi, 6000)   # make a random array from 0 to 5999

y = np.sin(2*np.pi*150*x) # this is my output as a funtion of the array

fy = np.fft.fft(y)     # take the fourier transform of the function

ify = np.fft.ifft(fy)   # take the inverse of the fourier transfrom 

fx = np.fft.fftfreq(x.size, x[1] - x[0])  # change our array to match the
                                          # frequency domain

plt.figure(1)           # Plot the Fourier Transfrom of the Function
plt. plot(np.fft.fftshift(abs(fx)), np.fft.fftshift(abs(fy)) , 'r')
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.title('The Fourier Transform in Action')

plt.figure(2)
plt.plot(x,y,'b')
plt.ylabel('Amplitude')
plt.xlabel('Time')
plt.title('The Function in Time Domain')

plt.grid()
plt.show()