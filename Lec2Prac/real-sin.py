#plotting real sinusoid

import numpy as np
import matplotlib.pyplot as plt

A = .8
fq = 1000
phi = np.pi/2

fs = 44100
t = np.arange(-.002, 0.002, 1.0/fs)
x = A * np.cos(2*np.pi*fq*t + phi)

plt.plot(t, x)
plt.axis([-.002, 0.002, -0.8, 0.8])
plt.xlabel("Time")
plt.ylabel("Amplitube")
plt.show()
