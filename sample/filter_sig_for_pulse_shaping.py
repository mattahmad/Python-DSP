import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

num_symbols = 10
sps = 8
N = 1024 # number of samples to simulate, choose any number you want
x = np.random.randn(N)
num_taps = 101
cut_off = 3000 # Hz
sample_rate = 32000 # Hz
# create our low pass filter
h = signal.firwin(num_taps, cut_off, nyq=sample_rate/2)
# Filter our signal, in order to apply the pulse shaping
x_shaped = np.convolve(x, h)
plt.figure(2)
plt.plot(x_shaped, '.-')
for i in range(num_symbols):
    plt.plot([i*sps+num_taps//2,i*sps+num_taps//2], [0, x_shaped[i*sps+num_taps//2]])
plt.grid(True)
plt.show()