import numpy as np
import matplotlib.pyplot as plt
x = np.zeros_like(n);
x[2]=3;
plt.vlines(n,0,x,'b');
plt.ylim(-1,4);
plt.plot(n,0*n, 'b');
plt.show();
