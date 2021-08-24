from matplotlib.pylab import *
T0 = 10
t = linspace(0,T0,1000)
for k in range(1,5):
    subplot(4,1,k)
    plot(t, sin(2*k*pi*t / T0))
show()
