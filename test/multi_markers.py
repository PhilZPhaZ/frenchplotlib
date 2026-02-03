import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import dorures, tapisseries

fig, ax = plt.subplots(figsize=(12, 8))

# Différents marqueurs
marqueurs = [tapisseries.croissant, tapisseries.vin, tapisseries.fromage, tapisseries.macaron]
couleurs = ['#FFD700', '#8B0000', '#F5DEB3', '#FFB6C1']
labels = ['Croissant', 'Vin', 'Fromage', 'Macaron']

for i, (marker, color, label) in enumerate(zip(marqueurs, couleurs, labels)):
    x = np.random.randn(10) + i*2
    y = np.random.randn(10) + i
    ax.scatter(x, y, marker=marker, s=800, c=color, label=label, alpha=0.7)

ax.legend(loc='best')
ax.set_title('Les délices de France', fontsize=16)
plt.show()