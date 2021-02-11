import numpy as np
from prettytable import PrettyTable as PT
import prettytable as pt
import matplotlib.pyplot as plt

# Settings
N = 20
N_D = 6
NBINS = 10

x = np.linspace(0, 1, N)

# Go through multiple # of dimensions
plt.figure(2)
table = PT()
for D in range(1, N_D):
	NT = 1
	print(x)

	z = np.array([1])
	for i in range(D):
		NT *= N # book-keeping
		z = np.outer(x, z).flatten()

	zs = np.sort(z)*100/np.sum(z)
	b = np.arange(0, NBINS, 1)
	zsc = np.sum(np.reshape(zs, (NBINS, int(NT/NBINS))), axis=1)

	table.field_names = [""] + ["Q%d" % (i+1) for i in b]
	table.add_row(["D = %d" % D] + ["%.4f %%"%i for i in zsc])

	plt.plot(b, zsc)
	plt.ylim([0, 100])

plt.legend(["D = %d"%i for i in range(1, N_D)])

print(table)
plt.show()