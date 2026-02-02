# 🥖 frenchplotlib

Une bibliothèque Python pour ajouter une touche française à vos visualisations matplotlib avec des marqueurs personnalisés et des palettes de couleurs inspirées de la France.

## 📝 Description

**frenchplotlib** enrichit vos graphiques matplotlib avec :
- 🥐 **17 marqueurs personnalisés** en forme d'icônes françaises (baguette, croissant, vin, fromage, etc.)
- 🎨 **15 palettes de couleurs** inspirées de la culture française (tricolore, lavande de Provence, Bordeaux, etc.)

## 🚀 Installation

```bash
pip install frenchplotlib
```

## 📦 Prérequis

- Python >= 3.6
- matplotlib
- numpy

## 💡 Utilisation

### Marqueurs personnalisés

```python
import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import baguetteplot

# Données d'exemple
x = np.linspace(-1, 1, 20)
y = np.sin(x)

# Utilisation d'un marqueur en forme de boule de pain
plt.figure(figsize=(10, 6))
plt.scatter(x, y, marker=baguetteplot.boule, s=500)
plt.title("Graphique avec marqueur français")
plt.show()
```

### Palettes de couleurs

```python
import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import baguetteplot, dorures

# Données d'exemple
x = np.linspace(-1, 1, 20)
y = np.sin(x)

# Combinaison marqueur + palette de couleurs
plt.figure(figsize=(12, 6))
plt.scatter(x, y, c=y, marker=baguetteplot.boule, s=1000, cmap=dorures.escargot_persil)
plt.colorbar(label='Valeurs')
plt.title("Visualisation à la française")
plt.show()
```

## 🥐 Marqueurs disponibles (baguetteplot)

- `baguette` - Une baguette traditionnelle
- `pain_de_mie` - Pain de mie
- `croissant` - Croissant doré
- `pain_au_chocolat` - Pain au chocolat (ou chocolatine 😉)
- `boule` - Boule de pain
- `brioche` - Brioche dorée
- `bretzel` - Bretzel alsacien
- `fougasse` - Fougasse provençale
- `pita` - Pain pita
- `vin` - Verre de vin
- `fromage` - Morceau de fromage
- `eclair` - Éclair au chocolat
- `macaron` - Macaron parisien
- `camembert` - Camembert de Normandie
- `madeleine` - Madeleine de Proust
- `religieuse` - Religieuse au chocolat
- `escargot` - Escargot de Bourgogne

## 🎨 Palettes de couleurs (dorures)

### Palettes gourmandes
- `pain_dore` - Du blanc crème au brun doré
- `baguette_bien_cuite` - Dégradé de cuisson parfaite
- `croissant_beurre` - Or brillant et miel
- `fromage` - Palette des fromages français
- `macaron` - Couleurs pastel gourmandes

### Palettes régionales
- `tricolore` - Drapeau français (bleu, blanc, rouge)
- `lavande` - Lavande de Provence
- `cote_azur` - Mer et ciel méditerranéens
- `bourgogne` - Couleurs d'automne bourguignonnes
- `versailles` - Or et splendeur royale

### Palettes viticoles
- `bordeaux` - Du rosé au rouge profond
- `champagne` - Pétillant et doré

### Palettes spéciales
- `escargot_persil` - Marron gris-vert
- `french_kiss` - Rouge passionnel
- `je_m_en_fous` - Gris perle élégant

## 📊 Exemples avancés

### Graphique multi-marqueurs

```python
import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import baguetteplot, dorures

fig, ax = plt.subplots(figsize=(12, 8))

# Différents marqueurs
marqueurs = [baguetteplot.croissant, baguetteplot.vin, baguetteplot.fromage, baguetteplot.macaron]
couleurs = ['#FFD700', '#8B0000', '#F5DEB3', '#FFB6C1']
labels = ['Croissant', 'Vin', 'Fromage', 'Macaron']

for i, (marker, color, label) in enumerate(zip(marqueurs, couleurs, labels)):
    x = np.random.randn(10) + i*2
    y = np.random.randn(10) + i
    ax.scatter(x, y, marker=marker, s=800, c=color, label=label, alpha=0.7)

ax.legend(loc='best')
ax.set_title('Les délices de France', fontsize=16)
plt.show()
```

### Heatmap avec palette française

```python
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
```

## 🛠️ Développement

### Installation en mode développement

```bash
git clone https://github.com/votre-username/frenchplotlib.git
cd frenchplotlib
pip install -e .
```

### Structure du projet

```
frenchplotlib/
├── frenchplotlib/
│   ├── __init__.py
│   ├── baguetteplot.py    # Marqueurs personnalisés
│   └── dorures.py          # Palettes de couleurs
├── main.py                 # Exemple d'utilisation
├── setup.py
├── pyproject.toml
└── README.md
```

## 📄 Licence

Ce projet est sous licence MIT.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Signaler des bugs
- Proposer de nouvelles fonctionnalités
- Ajouter de nouveaux marqueurs ou palettes
- Améliorer la documentation

## 🙏 Remerciements

Merci à matplotlib pour son excellente bibliothèque de visualisation qui rend tout cela possible.

---

*Créé avec ❤️ et 🥖 en France*
