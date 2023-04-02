#%%

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.signal
import copy

from scipy import *

#%%

# Creating signal

signalRate : int = 1000 # hz
time :np.array =  np.arange(0, 3, 1/signalRate)

n : int = len(time) # Signal Lenght
print(n)
p : int = 15 # Poles(Titik titik tertentu) untuk random ionterpolation

np.random.seed(5)
## Noise level
noiseAmplitude : int = 5

## Amplitdude modulator and noise level
print(np.linspace(0,p,n))
ampl : np.array = np.interp(np.linspace(0,p,n), 
                            xp=np.arange(0,p),
                            fp=np.random.rand(p)*30)
noise : np.array = noiseAmplitude * np.random.randn(n)
signal : np.array = ampl + noise
#plt.plot(time, ampl, label="orig")

# create filtered signal vector

filteredSignal : np.array = np.zeros(n)

# Implement Running mean filter

k = 20 
for i in range(k, n - k) :
    filteredSignal[i] = np.mean(signal[i-k : i+k+1]) ## Plus 1 , i+k-1 ( default ) biasanya

windowSize : np.array = 1000 * (k * 2 + 1) / signalRate ## Convert pada waktu lagi

plt.plot(time, signal, label="origin")
plt.plot(time, filteredSignal, label="filtered")
plt.legend()
plt.xlabel("Time (sec)")
plt.ylabel("Amplitude")
plt.title('Running-mean filter with a k=%d-ms filter' %windowSize)

plt.show()

# %%
