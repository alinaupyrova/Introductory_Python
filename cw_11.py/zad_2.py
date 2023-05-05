import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123)

series = np.random.rand(5, 50)

colors = ['r', 'b', 'g', 'y', 'm']
markers = ['o', '^', 's', 'd', 'v']
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
for i in range(5):
    ax.scatter(range(50), series[i], c=colors[i], marker=markers[i])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
