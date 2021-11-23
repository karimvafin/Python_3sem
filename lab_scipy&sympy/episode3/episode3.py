from scipy.integrate import odeint
import numpy as np
import sympy as sym
from sympy.abc import x
from matplotlib import pyplot as plt

# sympy
f = sym.Function('f')

solution = sym.dsolve(f(x).diff(x) + 2 * f(x), f(x), ics={f(0): sym.sqrt(2)})

X = np.arange(0, 10, 0.1)
Y_simpy = [float(solution.args[1].subs(x, i)) for i in X]

# scipy
def dydt(y, t):
    return -2 * y


y0 = float(sym.sqrt(2))
Y_scipy = np.array(odeint(dydt, y0, X)).flatten()

fig, axes = plt.subplots(2)
axes[0].plot(X, Y_simpy, color='red', label='Sympy')
axes[0].plot(X, Y_scipy, color='blue', label='Scipy')
axes[0].grid()
axes[0].legend()
axes[0].set_title('Решение')
axes[1].plot(X, abs(Y_scipy-Y_simpy))
axes[1].grid()
axes[1].set_title('Модуль разности двух решений')
plt.subplots_adjust(hspace=0.5)
plt.savefig('plot.png')
