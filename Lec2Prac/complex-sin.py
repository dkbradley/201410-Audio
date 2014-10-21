#complex sinusoid

import numpy as np
import matplotlib.pyplot as plt

N = 500	#number of samples per period
k = 3		#frequency, number of periods

#N = 32		#fewer number of samples per period - creates a sinusoid with sharp edges
#k = 5		#frequency, more periods

n = np.arange(-N/2, N/2)

s = np.exp(1j * 2 * np.pi * k * n/N)

plt.plot(n, np.real(s)) 	#plotting only real part of complex sinusoid
plt.plot(n, np.imag(s)) 	#plotting only imaginary part of complex sinusoid

plt.axis([-N/2, N/2, -1, 1])
plt.xlabel("Indexes")
plt.ylabel("Amplitube")
plt.show()

