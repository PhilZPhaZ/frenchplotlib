import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import styles

# Appliquer le style Côte d'Azur
styles.style_cote_azur()

# Créer des données
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Créer le graphique
plt.figure(figsize=(10, 6))
plt.plot(x, y1, linewidth=3, label='Vague 1')
plt.plot(x, y2, linewidth=3, label='Vague 2')
plt.fill_between(x, y1, alpha=0.3)
plt.fill_between(x, y2, alpha=0.3)

plt.title('🌊 Les Vagues de la Méditerranée', fontsize=16)
plt.xlabel('Distance (km)', fontsize=12)
plt.ylabel('Amplitude (m)', fontsize=12)
plt.legend()
plt.grid(True)

# Restaurer le style par défaut
styles.restaurer_style()
