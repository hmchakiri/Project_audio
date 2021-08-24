import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(-0.02, 0.05, 1000)
plt.subplot(2,1,1); plt.plot(t, np.abs(np.exp(2j*np.pi*50*t)) );
plt.xlabel(r'$t$');
plt.ylabel(r'$|x(t)|$');
plt.title(r'Absolute value  of  $x(t)=e^{j 100 \pi t}$');
plt.xlim([-0.02, 0.05]);
plt.subplot(2,1,2); plt.plot(t, np.angle(np.exp(2j*np.pi*50*t))*360/(2*np.pi) );
plt.xlabel('$t$');
plt.ylabel(r'$\angle x(t)$');
plt.title(r'Phase of  $x(t)=e^{j 100 \pi t}$');
plt.xlim([-0.02, 0.05]);
plt.show()
