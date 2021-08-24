import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-0.02, 0.05, 1000)
plt.subplot(2,1,1); plt.plot(t, np.exp(2j*np.pi*50*t).real );
plt.xlabel('t');
plt.ylabel('Re x(t)');
plt.title(r'Real part of  $x(t)=e^{j 100 \pi t}$');
plt.xlim([-0.02, 0.05]);
plt.subplot(2,1,2); plt.plot(t, np.exp(2j*np.pi*50*t).imag );
plt.xlabel('t');
plt.ylabel('Im x(t)');
plt.title(r'Imaginary part of  $x(t)=e^{j 100 \pi t}$');
plt.xlim([-0.02, 0.05]);
plt.show()
