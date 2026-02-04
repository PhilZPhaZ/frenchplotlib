import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib.custom_marker import load_svg_marker

marker = load_svg_marker('frenchplotlib/assets/baguette.svg')

# Données d'exemple
x = np.linspace(-1, 1, 20)
y = np.sin(x)

# Utilisation d'un marqueur en forme de boule de pain
plt.figure(figsize=(10, 6))
plt.scatter(x, y, marker=marker, s=500)
plt.title("Graphique avec marqueur français")
plt.show()
