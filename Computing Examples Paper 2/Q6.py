import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt
import sounddevice as sd
#import urllib
#import urllib.request

local_wav = "C:/Users/Wjb35/Downloads/Armstrong_Small_Step.wav"

# Read frequency and data array for sound track
fs, x = scipy.io.wavfile.read(local_wav) 

# If we have a stereo track (left and right channels), take just the first channel
if len(x.shape) > 1:
    x = x[:, 0]

#sd.play(x,fs)
#sd.wait()

# Time points (0 to T, with T*fs points)
t = np.linspace(0, len(x)/fs, len(x), endpoint=False)

# Plot signal
plt.plot(t, x)
plt.xlabel('time (s)')
plt.ylabel('signal')
#plt.show()

# Perform a Fourier transform of the signal (signal is real, so we can use the 'real' version)
xf = np.fft.rfft(x)

# Create frequency axis
freq = np.linspace(0.0, fs/2, len(xf))

# Plot Fourier coefficients against frequency. Fourier coefficients are complex, so
# we take the modulus.
plt.plot(freq, np.abs(xf))
plt.xlabel('frequency (Hz)')
plt.ylabel('$\hat{x}$')
#plt.show()

# Copy transformed problem
xf_filtered = xf.copy()

# Cut off frequencies
cutoff_freq = 85 # A google search said the human range is about 85 - 250 Hz, so chose 85Hz
n_cut = int(2*cutoff_freq*len(xf_filtered)/fs)
xf_filtered[:n_cut] = 0.0

plt.plot(freq, np.abs(xf_filtered))
plt.xlabel('frequency (Hz)')
plt.ylabel('$\hat{x}$')
plt.xlim(0, 2*cutoff_freq)
#plt.show()

# Perform inverse transfiorm
x_filtered = np.fft.irfft(xf_filtered)

# Plot signal over first 0.05 s
n = int(0.05*fs)
plt.plot(t[:n], x_filtered[:n])
plt.xlabel('time (s)')
plt.ylabel('$x(t)$')
#plt.show()

sd.play(x_filtered, fs)
sd.wait()