import numpy as np
import matplotlib.pyplot as plt

# Create a sample signal
sampling_rate = 1000  # Hz
duration = 1       # seconds
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
frequency1 = 50    # Hz
frequency2 = 120   # Hz
signal = np.sin(2 * np.pi * frequency1 * t) + 0.5 * np.sin(2 * np.pi * frequency2 * t)

# Perform the FFT
fft_output = np.fft.fft(signal)

# Calculate frequencies corresponding to the FFT output
frequencies = np.fft.fftfreq(len(signal), d=1/sampling_rate)

# Take the absolute value to get the magnitude of the frequency components
magnitudes = np.abs(fft_output)

# Plot the original signal and its frequency spectrum
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(1, 2, 2)
# Plot only positive frequencies for clarity
plt.plot(frequencies[:len(frequencies)//2], magnitudes[:len(magnitudes)//2])
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()