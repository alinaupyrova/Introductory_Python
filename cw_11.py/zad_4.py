import numpy as np
import matplotlib.pyplot as plt

# Wygenerowane dane
x = np.arange(4)
y = np.arange(5)
xx, yy = np.meshgrid(x, y)
x, y = xx.ravel(), yy.ravel()
top = x + y
bottom = np.zeros_like(top)
width = depth = 1

fig = plt.figure(figsize=(10, 8))

# Wykres 1
ax1 = fig.add_subplot(221, projection='3d')
ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Shaded plot, alpha=1')

# Wykres 2
ax2 = fig.add_subplot(222, projection='3d')
ax2.bar3d(x, y, bottom, width, depth, top, shade=True, alpha=0.5)
ax2.set_title('Shaded plot, alpha=0.5')

# Wykres 3
ax3 = fig.add_subplot(223, projection='3d')
ax3.bar3d(x, y, bottom, width, depth, top, shade=False, edgecolor='black')
ax3.set_title('Non-shaded plot, black edges')

# Wykres 4
ax4 = fig.add_subplot(224, projection='3d')
ax4.bar3d(x, y, bottom, width, depth, top, shade=False, edgecolor='red')
ax4.set_title('Non-shaded plot, red edges')

plt.show()
