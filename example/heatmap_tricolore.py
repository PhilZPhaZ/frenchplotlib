import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import dorures

# Données aléatoires
data = np.random.rand(10, 10)

plt.figure(figsize=(10, 8))
plt.imshow(data, cmap=dorures.tricolore, aspect='auto')
plt.colorbar(label='Intensité')
plt.title('Heatmap tricolore')
plt.show()