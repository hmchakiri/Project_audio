from scipy.fft import ifftn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
N = 30
f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex='col', sharey='row')
xf = np.zeros((N,N))
xf[0, 5] = 1
xf[0, N-5] = 1
#To do 1: add this instruction xf = fftshift(xf)
Z = ifftn(xf)
#To do 1: add this instruction Z = fftshift(Z)
ax1.imshow(xf, cmap=cm.Reds)
ax4.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 0] = 1
xf[N-5, 0] = 1
#To do 2: add this instruction xf = fftshift(xf)
Z = ifftn(xf)
#To do 2: add this instruction Z = fftshift(Z)
ax2.imshow(xf, cmap=cm.Reds)
ax5.imshow(np.real(Z), cmap=cm.gray)
xf = np.zeros((N, N))
xf[5, 10] = 1
xf[N-5, N-10] = 1
#To do 3: add this instruction xf = fftshift(xf)
Z = ifftn(xf)
#To do 3: add this instruction Z = fftshift(Z)
ax3.imshow(xf, cmap=cm.Reds)
ax6.imshow(np.real(Z), cmap=cm.gray)
plt.show()
