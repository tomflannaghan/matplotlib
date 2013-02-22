import numpy as np
import matplotlib.pyplot as plt

Y, X = np.mgrid[0:1:100j, 0:1:100j]

#X **= 2
#Y **= 0.5

X = 6 * X - 3
Y = 6 * Y - 3

U = -1 - X**2 + Y
V = 1 + X - Y**2
speed = np.sqrt(U*U + V*V)

import time
t = time.time()
plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=plt.cm.autumn)
plt.colorbar()
print time.time() - t

f, (ax1, ax2) = plt.subplots(ncols=2)
ax1.streamplot(X, Y, U, V, density=[0.5, 1])

lw = 5*speed/speed.max()
ax2.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)

plt.show()

