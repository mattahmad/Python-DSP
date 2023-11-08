import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


num_taps = 51 # it helps to use an odd number of taps
cut_off = 3000 # Hz
sample_rate = 32000 # Hz

H = np.hstack((np.zeros(20), np.arange(10)/10, np.zeros(20)))

h = np.fft.ifftshift(np.fft.ifft(np.fft.ifftshift(H)))
plt.plot(np.real(h))
plt.plot(np.imag(h))
plt.legend(['real','imag'], loc=1)
plt.show()