from matplotlib import pyplot as plt

X = []
Y = []

with open('data.txt') as file:
    data = file.read().split('\n')
    size = int(len(data) / 2)
    for i in range(size):
        X.append([float(elem) for elem in data[2 * i].split()])
        Y.append([float(elem) for elem in data[2 * i + 1].split()])

MAX_X, MIN_X = max(max(x_list) for x_list in X), min(min(x_list) for x_list in X)
MAX_Y, MIN_Y = max(max(y_list) for y_list in Y), min(min(y_list) for y_list in Y)

fig, axes = plt.subplots(3, 2)
fig.set_figheight(8)
plt.subplots_adjust(wspace=0.3, hspace=0.3)
axes_m = [0, 0, 1, 1, 2, 2]
axes_n = [0, 1, 0, 1, 0, 1]
for i, m, n in zip(range(size), axes_m, axes_n):
    axes[m][n].plot(X[i], Y[i])
    axes[m][n].set_title(f'Frame {i}')
    axes[m][n].grid()
    axes[m][n].set_xlim(MIN_X, MAX_X)
    axes[m][n].set_ylim(1.2 * MIN_Y, 1.2 * MAX_Y)
    axes[m][n].set_xticks(range(int(MIN_X), int(MAX_X), 2))
    axes[m][n].set_yticks(range(int(MIN_Y), int(MAX_Y), 3))

plt.savefig('episode_2.png')

