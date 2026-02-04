import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import tapisseries, dorures

# Données d'exemple
x = np.linspace(0, 10, 10)
y = np.random.rand(10) * 10
yerr = np.random.rand(10) * 2

# Création du graphique avec des barres d'erreur
plt.figure(figsize=(10, 6))
plt.errorbar(x, y, yerr=yerr, fmt='o', ecolor='red', capsize=5, marker=tapisseries.baguette, markersize=20)
plt.title("Graphique avec des barres d'erreur et des marqueurs personnalisés")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()
