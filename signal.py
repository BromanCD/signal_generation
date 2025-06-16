import numpy as np
import matplotlib.pyplot as plt

T = 1               
fs = 10000           
time = np.linspace(0, T, int(T * fs), endpoint=False)

frequency_sine = 100  
sine_wave = np.sin(2 * np.pi * frequency_sine * time)

f_carrier = 1000      
carrier = np.sin(2 * np.pi * f_carrier * time)

am = (1 + sine_wave) * carrier

f, ts, Sxx = spectrogram(am_signal, fs=fs, nperseg=256)

plt.tight_layout()
plt.pcolormesh(ts, f, 10 * np.log10(Sxx), shading='gouraud')
plt.colorbar(label='Power/Frequency (dB/Hz)')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [s]')
plt.show()
