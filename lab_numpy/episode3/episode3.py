import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt

N = 255
start = np.loadtxt("start.dat")
A1 = np.identity(start.shape[0])
A1[0][-1] = -1.
A2 = (-1) * np.eye(start.shape[0], k=-1, dtype=float)
A = A1 + A2

current = start

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0, 10))
line, = ax.plot([], [])


def update(i):
    global current, line
    current = current - 0.5 * A @ current
    line.set_data(np.arange(current.shape[0]), current)
    return line,


anim = FuncAnimation(fig, update, frames=N, interval=1, blit=True)
anim.save('func.gif', writer='pillow')

