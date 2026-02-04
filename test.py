import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import styles, tapisseries, dorures

# Appliquer un style complet
styles.style_versailles()

# Créer une visualisation élégante
fig, ax = plt.subplots(figsize=(12, 8))

x_scatter = np.random.rand(20) * 10
y_scatter = np.random.rand(20) * 2 - 1

# Utiliser marqueurs français avec le style appliqué
ax.scatter(x_scatter[:5], y_scatter[:5], marker=tapisseries.croissant, s=500, label='Croissants')
ax.scatter(x_scatter[5:10], y_scatter[5:10], marker=tapisseries.vin, s=500, label='Vin')
ax.scatter(x_scatter[10:15], y_scatter[10:15], marker=tapisseries.fromage, s=500, label='Fromage')

ax.set_title('👑 Délices Royaux de Versailles', fontsize=16)
ax.set_xlabel('Temps (heures)')
ax.set_ylabel('Satisfaction')
ax.legend()
ax.grid(True)

plt.show()

# Restaurer le style
styles.restaurer_style()