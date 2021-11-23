import numpy as np
from scipy.linalg import solve
from matplotlib import pyplot as plt

data = np.loadtxt('2.txt', skiprows=1)
N = data.shape[1]

matrix = data[:N, :]

b = data[-1, :]

x = solve(matrix, b)

plt.bar(range(x.shape[0]), x)
plt.grid()
plt.show()
