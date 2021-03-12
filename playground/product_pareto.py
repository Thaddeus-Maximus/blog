import numpy as np
from prettytable import PrettyTable as PT
import prettytable as pt
import matplotlib.pyplot as plt

N = 10
x = np.arange(1, N+1, 1)
z = np.outer(x, x)

mtable = PT()
mtable.vrules = pt.NONE
mtable.field_names = [" "] + [a for a in x]
for j in range(N):
	mtable.add_row([str(j)+" |"] + list(z[0:N+1, j]))
print(mtable)

zs = np.sort(z.flatten())

NBINS = 10

b = np.arange(0, NBINS, 1)
zsc = np.sum(np.reshape(zs, (NBINS, int(N*N/NBINS))), axis=1)

plt.bar(b, zsc)

plt.show()