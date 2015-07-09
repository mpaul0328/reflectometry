import matplotlib.pyplot as plt, numpy as np
                                                                   
N  = 5000 # Number of test points   
t = np.linspace(0, 2*np.pi, N) # x- axis in time domain
v = np.fft.fftshift(np.fft.fftfreq(t.size, t[1] - t[0])) # x-axis in frequency domain
zero_out = np.zeros(N)
zero_out[N/4 : (3*N)/4] = 1 # First & Last quarter points (zeros)                                                                                                     
f  = np.sin(2*np.pi*50*t)   
f *= zero_out # Create Signal f w/ ends (zeros)   
vf = np.fft.fft(f) # Signal f in frequecy domain                                     
g  = np.cos(2*np.pi*80*t)
g *= zero_out # Create Signal g w/ ends (zeros) 
vg= np.fft.fft(g) # Signal g in frequecy domain    

# Convolution THM 
conv = np.convolve(f, g,'same') # {f o g}
vfg = vf * vg 
fg = np.fft.ifft(vfg) # v^-1{vf * vg} 
vconv = np.fft.fft(conv) # v{f o g}

# Remove Multi-Line comment to show Proof of Equivalence
"""
plt.figure(5)
plt.title("Proof: v{f o g} = vf * vg")
plt.plot(v, np.fft.fftshift(np.abs(vfg)), 'r', v, np.fft.fftshift(np.abs(vconv)), 'y')

plt.figure(6)
plt.title("Proof: {f o g} = v^-1{vf * vg}")
plt.plot(t, conv, 'r', t, np.fft.fftshift(fg), 'b' )     
"""
# Remove Multi-Line comment to show graphs of Time & Freq of f & g
"""
plt.figure(1)
plt.plot(v, np.fft.fftshift(np.abs(vf)),'k')
plt.title('Frequency Domain of F')

plt.figure(2)
plt.plot(t,f,'k')
plt.title('Time Domain of F')

plt.figure(3)
plt.plot(v, np.fft.fftshift(np.abs(vg)),'b')
plt.title('Frequency Domain of G')

plt.figure(4)
plt.plot(t,g,'b')
plt.title('Time Domain of G')
"""
plt.show()      

