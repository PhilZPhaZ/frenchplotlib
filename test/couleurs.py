import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import dorures, tapisseries

# Données d'exemple
x = np.linspace(-1, 1, 20)
y = np.sin(x)

# Combinaison marqueur + palette de couleurs
plt.figure(figsize=(12, 6))
plt.scatter(x, y, c=y, marker=tapisseries.macaron, s=1000, cmap=dorures.versailles)
plt.colorbar(label='Valeurs')
plt.title("Visualisation à la française")
plt.show()