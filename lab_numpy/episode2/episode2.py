import numpy as np
from matplotlib import pyplot as plt

fig, ax = plt.subplots(3, 2)
fig.set_figheight(8)
for i in range(1, 4):
    data = np.loadtxt(f"signals/signal0{i}.dat")
    new_data = np.ones(data.shape[0])
    new_data[0] = data[0]
    new_data[1:10] = np.array([data[:i].mean() for i in range(1, 10)])
    new_data[10:] = np.array([data[i - 9:i].mean() for i in range(10, new_data.shape[0])])
    ax[i-1][0].plot(np.arange(data.shape[0]), data)
    ax[i-1][1].plot(np.arange(data.shape[0]), new_data)
    ax[i-1][0].grid()
    ax[i-1][1].grid()

ax[0][0].set_title("Сырой сигнал")
ax[0][1].set_title("После фильтра")
plt.savefig("plot.png")
