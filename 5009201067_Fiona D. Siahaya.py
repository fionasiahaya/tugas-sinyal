#ID
print("Nama: Fiona")
print("NRP: 5009201067")

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
# Create a signal
t = np.linspace(0, 1, 50)
x = np.sin(5 * np.pi * t) + np.cos(10 * np.pi * t)
# Compute the FFT
X = fft(x)
# Plot the magnitude and phase of the FFT
plt.subplot(2, 1, 1)
plt.plot(np.abs(X))
plt.title("Magnitude of the FFT")
plt.subplot(2, 1, 2)
plt.plot(np.angle(X))
plt.title("Phase of the FFT")
plt.show()
