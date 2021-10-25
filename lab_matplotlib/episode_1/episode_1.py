from matplotlib import pyplot as plt
import os
import math


for filename in os.listdir(path='dead_moroz'):
    X = []
    Y = []
    with open('dead_moroz/' + filename) as file:
        file_string = file.read().split('\n')
        for i in range(1, int(file_string[0]) + 1):
            X.append(float(file_string[i].split()[0]))
            Y.append(float(file_string[i].split()[1]))

    scale = (max(Y) - min(Y)) / (max(X) - min(X))
    plt.figure()

    r = math.sqrt(X[0] ** 2 + Y[0] ** 2)
    for x, y in zip(X, Y):
        for i, j in zip(X, Y):
            current_r = math.sqrt((x - i) ** 2 + (y - j) ** 2)
            if r > current_r > 0:
                r = current_r

    plt.title(f'Number of points: {len(X)}')
    plt.plot(X, Y, '.', markersize=r)
    plt.axis('scaled')
    plt.savefig(filename.replace('.dat', '') + '.png')
