import matplotlib.pyplot as plt
import numpy as np

N= 5
t = np.linspace(0.0, 2*np.pi, N)
f = np.sin(t)
g = np.cos(t)

ConV = np.convolve(f, g, 'same')
print ConV