import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import styles, tapisseries

# Données d'exemple
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

# Liste des styles à démontrer
styles_list = [
    ('versailles', styles.style_versailles, '👑 Style Versailles'),
    ('bistrot', styles.style_bistrot, '☕ Style Bistrot'),
    ('cote_azur', styles.style_cote_azur, '🌊 Style Côte d\'Azur'),
    ('provence', styles.style_provence, '💜 Style Provence'),
    ('parisien', styles.style_parisien, '🗼 Style Parisien'),
    ('tricolore', styles.style_tricolore, '🇫🇷 Style Tricolore'),
    ('bordeaux', styles.style_bordeaux, '🍷 Style Bordeaux'),
    ('belle_epoque', styles.style_belle_epoque, '🎨 Style Belle Époque'),
]

# Créer une figure avec tous les styles
fig = plt.figure(figsize=(20, 12))
fig.suptitle('🥖 Styles Graphiques Français - frenchplotlib', fontsize=20, fontweight='bold')

for idx, (name, style_func, title) in enumerate(styles_list, 1):
    # Appliquer le style
    style_func()
    
    # Créer le sous-graphique
    ax = fig.add_subplot(3, 3, idx)
    ax.plot(x, y1, linewidth=2, label='sin(x)')
    ax.plot(x, y2, linewidth=2, label='cos(x)')
    ax.plot(x, y3, linewidth=2, label='sin(x)cos(x)')
    
    ax.set_title(title, pad=10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend(loc='upper right')
    ax.grid(True)

plt.tight_layout()
plt.show()

# Restaurer le style par défaut
styles.restaurer_style()

# Style Versailles avec marqueurs
styles.style_versailles()
fig, ax = plt.subplots(figsize=(12, 8))

x_scatter = np.random.rand(20) * 10
y_scatter = np.random.rand(20) * 2 - 1

ax.scatter(x_scatter[:5], y_scatter[:5], marker=tapisseries.croissant, s=500, label='Croissants')
ax.scatter(x_scatter[5:10], y_scatter[5:10], marker=tapisseries.baguette, s=500, label='Baguettes')
ax.scatter(x_scatter[10:15], y_scatter[10:15], marker=tapisseries.vin, s=500, label='Vin')
ax.scatter(x_scatter[15:], y_scatter[15:], marker=tapisseries.fromage, s=500, label='Fromage')

ax.set_title('👑 Style Versailles avec Marqueurs Français', fontsize=16, pad=15)
ax.set_xlabel('Temps (heures)', fontsize=12)
ax.set_ylabel('Satisfaction', fontsize=12)
ax.legend(loc='best', fontsize=11)
ax.grid(True)

plt.tight_layout()
plt.show()

# Restaurer le style
styles.restaurer_style()

