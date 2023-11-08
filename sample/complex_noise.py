import numpy as np
import matplotlib.pyplot as plt

N = 1024 # number of samples to simulate, choose any number you want
n = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2)
plt.plot(np.real(n),'.-')
plt.plot(np.imag(n),'.-')
plt.legend(['real','imag'])
plt.show()