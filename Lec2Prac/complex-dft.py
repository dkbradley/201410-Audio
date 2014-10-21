#DFT implementation for a complex sinusoid

import numpy as np
import matplotlib.pyplot as plt

N = 64 #size of signal
fq = 7	#frequency/period
x = np.exp(1j * 2 * np.pi * fq / N * np.arange(N))

X = np.array([])

for k in range(N):
	s = np.exp(1j * 2 * np.pi * k / N * np.arange(N))
	X = np.append(X, sum(x * np.conjugate(s)))

plt.plot(np.arange(N), abs(X))

plt.axis([0, N, -1, N])
plt.xlabel("Indexes")
plt.ylabel("Amplitube")
plt.show()

