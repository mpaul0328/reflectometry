import matplotlib.pyplot as plt, numpy as np

N  = 500 # Number of test points  
t = np.linspace(0,2*np.pi, N) # x-axis in time domain
v = np.fft.fftshift(np.fft.fftfreq(t.size, t[1] - t[0])) # x-axis in frequency domain
p = np.zeros(N)
_p = np.zeros(N)
p[0] = 1 # Pulse @ bin 0
_p[20] = 1 # Pulse @ bin 20
vp = np.fft.fft(p) #
v_p = np.fft.fft(_p) 

plt.figure(1)
plt.plot(v, vp.real, v, vp.imag)
plt.plot(v, vp, 'm')
plt.title('Pulse @ bin 0')

plt.figure(2)
plt.plot(v, v_p.real, v, v_p.imag)
plt.plot(v, np.fft.fftshift(np.abs(v_p)), 'k')
plt.title('Pulse @ bin 20')

plt.figure(3)
plt.plot(t, p,'b', t,_p,'r')
plt.title("Time Domain of both Pulses")

plt.show()
