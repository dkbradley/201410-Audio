import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import triang
from scipy.fftpack import fft
from scipy.signal import get_window
import sys, os, math
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models'))
import utilFunctions as UF
import dftModel as DFT

#converts wav file to floating point array normilised -1 to 1
(fs, x) = UF.wavread('../../sounds/piano.wav') 

M = 511
w = get_window('hamming', M)

time = .2
x1 = x[int(time * fs):int(time * fs) + M]

N = 1024
mX, pX = DFT.dftAnal(x1, w, N)

y = DFT.dftSynth(mX, pX, w.size) * sum(w)

plt.plot(y)
plt.show()
