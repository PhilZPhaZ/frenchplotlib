import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import tapisseries, dorures

x = np.linspace(0, 10, 10)
y = np.random.rand(10) * 10
yerr = np.random.rand(10) * 2

plt.figure(figsize=(10, 6))

# Barres d'erreur sans marqueurs
plt.errorbar(x, y, yerr=yerr, fmt='none', ecolor='gray', capsize=5, alpha=0.5)

# Scatter avec colormap
plt.scatter(x, y, c=y, marker=tapisseries.baguette, s=500, cmap=dorures.lavande)
plt.colorbar(label='Valeurs')

plt.title("Errorbar avec colormap")
plt.show()