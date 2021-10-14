import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy


colors = {
    0: 'r',
    1: 'b',
    2: 'fuchsia',
    3: 'yellow',
    4: 'black',
    5: 'deepskyblue',
    6: 'purple',
    7: 'lime'
}


def dist(x, y, xc, yc):
    return np.sqrt((x - xc) ** 2 + (y - yc)**2)


def define_cluster(x, y, centers, cluster):
    for i in range(len(cluster)):
        d = np.array([])
        for j in range(len(centers)):
            d = np.append(
                d,
                dist(x[i], y[i], centers[j][0], centers[j][1])
            )
        cluster[i] = np.argmin(d)


def renovate_centers(x, y, centers, cluster):
    count = np.array([0] * len(centers))
    coord = np.array([0] * (len(centers) * 2))
    coord = coord.reshape(len(centers), 2)
    for i in range(len(cluster)):
        count[cluster[i]] += 1
        coord[cluster[i]][0] += x[i]
        coord[cluster[i]][1] += y[i]
    for i in range(len(centers)):
        if count[i] != 0:
            centers[i][0] = coord[i][0] / count[i]
            centers[i][1] = coord[i][1] / count[i]


def displacement(old, new):
    disp = 0
    for i in range(len(new)):
        disp += dist(
            old[i][0],
            old[i][1],
            new[i][0],
            new[i][1]
        )
    return disp


count = int(input("Количество точек: "))
x = np.random.randn(count)
y = np.random.randn(count)


fig, simple = plt.subplots()
simple.scatter(x,y)


k = int(input("Количество кластеров:(от 2 до 5) "))
centers = np.array([])
for i in range(k):
    centers = np.append(
        centers,
        [np.cos(2*i*np.pi/k), np.sin(2*i*np.pi/k)],
    )


centers = centers.reshape(k,2)
for j in range(len(centers)):
    plt.scatter(centers[j][0], centers[j][1], marker='*', s=200, c='black')
plt.show()

cluster = np.array([0]*count)


while True:
    define_cluster(x, y, centers, cluster)
    for j in range(len(centers)):
        plt.scatter(centers[j][0], centers[j][1], marker = '*', s=200, c='black')
    for i in range(count):
        plt.scatter(x[i], y[i], c = colors[cluster[i]])
    plt.show()
    old_centers = deepcopy(centers)
    renovate_centers(x, y, centers, cluster)
    if displacement(old_centers, centers) < 0.01:
        break