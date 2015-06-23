from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Number of test points
N  = 3001         
                                                       
# X points for functions (tx => Time Domain; vx => Freq Domain)
tx = np.linspace(0, np.pi/2, N)
vx = np.fft.fftshift(abs(np.fft.fftfreq(tx.size, tx[1] - tx[0])))


# T means the Fourier Transformed fucntion
# Create Signal f                                                                                                                 
f  = np.sin(2*np.pi*tx)                                                
T_f= np.fft.fftshift(abs(np.fft.fft(f)))                                                                    
# Create Signal g
g  = np.cos(2*np.pi*tx)
T_g= np.fft.fftshift(abs(np.fft.fft(g))) 

# ffftfreq => gave corresponding freq from timex   
# fft => fourier transformation                                                                      
# abs => gave only positive freq/ converted imaginary # to real # 
# fftshift => set zero at center

# Convolution of f o g & Transformation of ConV
ConV = np.convolve(f, g, 'full')
T_ConV= np.fft.fftshift(abs(np.fft.fft(ConV)))

# Multiplying Transforms of f & g 
ConVT = T_g * T_f

# Show that ConVT == T_ConV
"""
plt.figure(5)
plt.plot(ConVT,'g', T_ConV, 'k')
plt.title('Straight Convolution')
plt.xlabel('Time')
"""




# Remove Multi-Line comment to show graphs of Time & Freq of f & g
"""
plt.figure(1)
plt.plot(vx, T_f,'k')
plt.title('Frequency Domain of F')
plt.xlabel('Frequency')

plt.figure(2)
plt.plot(tx,f,'k')
plt.title('Time Domain of F')
plt.xlabel('Time')

plt.figure(3)
plt.plot(vx, T_g,'b')
plt.title('Frequency Domain of G')
plt.xlabel('Frequency')

plt.figure(4)
plt.plot(tx,g,'b')
plt.title('Time Domain of G')
plt.xlabel('Time')

plt. grid()
plt.show()
"""



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
