import matplotlib.pylab as plt
import sympy as sp
t, T0 = sp.symbols("t, T0")
x = sp.Piecewise(
    (1, t % T0<=T0/2),
    (0, True))
sp.plot(x.subs(T0,1), (t,-.2, 1.7), xlabel="t", ylabel="x(t)", line_width=3);
plt.show()
