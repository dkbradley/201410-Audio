import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)

fftbuffer = np.zeros(15)
fftbuffer[:8] = x[7:]
fftbuffer[8:] = x[:7]

X = fft(fftbuffer)

mX = abs(X)
pX = np.angle(X)

#plt.plot(x)
#plt.plot(fftbuffer)
#plt.plot(X)
#plt.plot(mX)
plt.plot(pX)

plt.show()

