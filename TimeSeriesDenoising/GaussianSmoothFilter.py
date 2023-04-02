#%%
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import scipy.signal
import copy

from scipy import *
#%%
np.random.seed(2)

def createSignal() -> np.array :
    signalRate : int = 1000 # in hertz, 
    time : np.array = np.arange(0, 3, 1/signalRate) # Periode of each signal siklus

    n : int  = len(time)
    poles : int = 15

    noiseAmplitude : int = 5

    sAmplitude = np.interp(
        np.linspace(1, poles, n),
        xp = np.arange(0,poles),
        fp = np.random.randn(poles) * 30

    )
    ## Create the signal 
    noise : np.array = noiseAmplitude * np.random.randn(n)

    return sAmplitude + noise


signal = createSignal()
#plt.plot(signal)

##  Create gaussian Krenel
## Full width half maximum : key gaussian parameter
fwhm : int = 25 #in ms

## Normalized time vector in ms

k : int = 40
signalRate = 1000
# Pembagi dengan nilai Srate, berarti kita hendak menkonversi input menjadi  representasi sinya, katakan
# SampleRate  100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik 100, maka terdapat 100 jumlah sinyal perdetik
## setiap sampel memiliki unit detik dan juga untuk setiap 1000 sample, memakan 1 detik
## *1000 karena detik --> Milidetik 
gTime : np.array = 1000*np.arange(-k, k + 1) / signalRate

gaussianWindow : np.array = np.exp( -(4*np.log(2)*gTime**2)/ fwhm**2)

## Compute empirical FWHM
print((gaussianWindow)**2)
prePeakHalf = np.argmin( (gaussianWindow-.5) **2)
pstPeakHalf = k  +np.argmin( (gaussianWindow[k:]-.5) ** 2)
print(pstPeakHalf)
print(prePeakHalf)

empiricalFWHM = gTime[pstPeakHalf] - gTime[prePeakHalf]
plt.plot(gTime, gaussianWindow, "ko-")
plt.plot([
    gTime[prePeakHalf], gTime[pstPeakHalf]], [
        gaussianWindow[prePeakHalf],
        gaussianWindow[pstPeakHalf]
    ],"m")
#