import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import tapisseries

# Données d'exemple
x = np.linspace(-1, 1, 20)
y = np.sin(x)

# Utilisation d'un marqueur en forme de boule de pain
plt.figure(figsize=(10, 6))
plt.scatter(x, y, marker=tapisseries.boule, s=500)
plt.title("Graphique avec marqueur français")
plt.show()