import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

T = 1            #TOTAL time duration (1 sec )   
fs = 10000       #sampling frequency
time = np.linspace(0, T, int(T * fs), endpoint=False) #this creates an array of evenly spaced time values in a manner (start, stop, num,)

frequency_sine = 100  #this is our wave that carries the message or info
sine_wave = np.sin(2 * np.pi * frequency_sine * time) #sine wave with amplitude 1 (formula used = A*Sin(2*pi*f*t))

f_carrier = 1000      #carrier wave frequency
carrier = np.sin(2 * np.pi * f_carrier * time)

am = (1 + sine_wave) * carrier #formula for Amplitude Modulation

f, ts, Sxx = spectrogram(am, fs=fs, nperseg=256) #This code used to generate spectogram didn't understood it at first so had to use gpt to plot the spectogram part

plt.tight_layout()
plt.pcolormesh(ts, f, 10 * np.log10(Sxx), shading='gouraud')
plt.colorbar(label='Power/Frequency (dB/Hz)')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.show()
