import numpy as np
import matplotlib.pyplot as plt
n = np.arange(50);
dt = 0.07/50
x = np.sin(2 * np.pi * 50 * n * dt)
plt.xlabel('n');
plt.ylabel('x[n]');
plt.title(r'Plot of DT signal $x[n] = 325 \sin(2\pi 50 n \Delta t)$');
plt.stem(n, x);
