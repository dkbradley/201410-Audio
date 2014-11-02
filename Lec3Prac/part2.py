import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import triang
from scipy.fftpack import fft
import sys, os, math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models'))
import utilFunctions as UF

M = 501
#center stuff around zer
hM1 = int(math.floor((M+1)/2))
hM2 = int(math.floor(M/2))

#converts wav file to floating point array normilised -1 to 1
(fs, x) = UF.wavread('../../sounds/soprano-E4.wav') 
#take a fragment from input array 
#hamming - padding next week
x1 = x[5000:5000+M] * np.hamming(M)

N = 1024
#center around zero
fftbuffer = np.zeros(N)
fftbuffer[:hM1] = x1[hM2:]
fftbuffer[N - hM2:] = x1[:hM2]

X = fft(fftbuffer)
mX = abs(X)						#magnitude
mDb = 20 * np.log10(abs(X))		#magnitude in dB
pX = np.angle(X)				#phase
pXU = np.unwrap(np.angle(X))	#phase unwrapping

#plt.plot(x1)
#plt.plot(fftbuffer)
#plt.plot(mX)
#plt.plot(pX)

#plt.show()

