from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import blackman
# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
w = blackman(N)
ywf = fft(y*w)
xf = fftfreq(N, T)[:N//2]
plt.semilogy(xf[1:N//2], 2.0/N * np.abs(yf[1:N//2]), '-b')
plt.semilogy(xf[1:N//2], 2.0/N * np.abs(ywf[1:N//2]), '-r')
plt.semilogy(xf[1:N//2], np.abs(w[1:N//2]), '-g')
plt.legend(['FFT', 'FFT w. window', 'Blackman window'])
plt.grid()
plt.show()
