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

plt.plot(X, Y_simpy, color='red', label='Sympy')
plt.plot(X, Y_scipy, color='blue', label='Scipy')
plt.grid()
plt.legend()
plt.show()

