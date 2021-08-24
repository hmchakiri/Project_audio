from scipy.fft import fft, ifft
import numpy as np
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
print("x(t)", end=": ")
print(x)
y = fft(x)
print("y(f)=TF[x(t)]", end=": ")
print(y)
yinv = ifft(y)
print("x'(t)=TF-1[y(f)]", end=": ")
print(yinv)
#sum
print("sum for x(t)=",np.sum(x))
print("sum for y(f)=",np.sum(y))
# compute the sum of |x|^2
