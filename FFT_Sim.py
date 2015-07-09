import matplotlib.pyplot as plt, numpy as np

N  = 5000 # Number of test points   
t = np.linspace(0, 2*np.pi, N) # x- axis in time domain
v = np.fft.fftshift(np.fft.fftfreq(t.size, t[1] - t[0])) # x-axis in frequency domain                                                                                                    
f  = np.sin(2*np.pi*50*t)     
vf = np.fft.fft(f) # Signal f in frequecy domain                                     
 
plt.figure(1)
plt.plot(t,f,'b')
plt.title("Time Domain")

plt.figure(2)
plt.plot(v, np.fft.fftshift(np.abs(vf)),'g')
plt.title('Frequency Domain')

plt.show()