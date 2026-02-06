import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib.styles import rendre_pretentieux

# Créer des données simples
x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.cos(x)

ax = plt.subplot(1, 1, 1)
ax.plot(x, y1, label='sin(x)', color='blue')
ax.plot(x, y2, label='cos(x)', color='red')
ax.set_title("Sinus et cosinus")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
rendre_pretentieux(ax)

plt.tight_layout()
plt.show()
