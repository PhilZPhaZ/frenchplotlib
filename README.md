# 🥖 frenchplotlib

Une bibliothèque Python pour ajouter une touche française à vos visualisations matplotlib avec des marqueurs personnalisés et des palettes de couleurs inspirées de la France.

## 📝 Description

**frenchplotlib** enrichit vos graphiques matplotlib avec :

- 🥐 **17 marqueurs personnalisés** en forme d'icônes françaises (baguette, croissant, vin, fromage, etc.)
- 🎨 **20 palettes de couleurs** inspirées de la culture française (tricolore, lavande de Provence, grève nationale, etc.)
- 🖼️ **8 styles graphiques prédéfinis** pour transformer l'apparence complète de vos graphiques (Versailles, Bistrot, Côte d'Azur, etc.)
- 🎭 **Mode prétentieux** pour rendre vos graphiques ridiculement français avec formulations ampoulées

## 🚀 Installation

```bash
pip install frenchplotlib
```

## 📦 Prérequis

- Python >= 3.6
- matplotlib
- numpy

### Pour les marqueurs SVG personnalisés (optionnel)

Si vous souhaitez utiliser `load_svg_marker()` pour charger vos propres fichiers SVG :

```bash
pip install svgpathtools svgpath2mpl
```

## 💡 Utilisation

### Marqueurs personnalisés prédéfinis

```python
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
```

### Marqueurs personnalisés depuis SVG

Vous pouvez également charger vos propres marqueurs SVG ou utiliser les marqueurs fournis dans le dossier `assets/` :

```python
import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib.custom_marker import load_svg_marker

# Charger un marqueur SVG personnalisé
marker = load_svg_marker('frenchplotlib/assets/baguette.svg')

# Ou utilisez votre propre fichier SVG
# marker = load_svg_marker('chemin/vers/votre/fichier.svg')

# Données d'exemple
x = np.linspace(-1, 1, 20)
y = np.sin(x)

# Utilisation du marqueur personnalisé
plt.figure(figsize=(10, 6))
plt.scatter(x, y, marker=marker, s=500)
plt.title("Graphique avec marqueur SVG personnalisé")
plt.show()
```

**Avantages des marqueurs SVG personnalisés :**
- 🎨 Utilisez n'importe quel fichier SVG comme marqueur
- 🔧 Plus de flexibilité pour créer vos propres designs
- 📦 Tous les marqueurs français sont disponibles en SVG dans `frenchplotlib/assets/`
- 🎯 Le marqueur est automatiquement centré et mis à l'échelle

**Fichiers SVG disponibles :**
- `baguette.svg`, `boule.svg`, `bretzel.svg`, `brioche.svg`
- `camembert.svg`, `croissant.svg`, `eclair.svg`, `escargot.svg`
- `fougasse.svg`, `fromage.svg`, `macaron.svg`, `madeleine.svg`
- `pain_au_chocolat.svg`, `pain_de_mie.svg`, `pita.svg`
- `religieuse.svg`, `vin.svg`

### Palettes de couleurs

```python
import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import tapisseries, dorures

# Données d'exemple
x = np.linspace(-1, 1, 20)
y = np.sin(x)

# Combinaison marqueur + palette de couleurs
plt.figure(figsize=(12, 6))
plt.scatter(x, y, c=y, marker=tapisseries.boule, s=1000, cmap=dorures.escargot_persil)
plt.colorbar(label='Valeurs')
plt.title("Visualisation à la française")
plt.show()
```

### Styles graphiques prédéfinis

Appliquez un style complet à tous vos graphiques pour une ambiance française authentique :

```python
import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import styles

# Appliquer le style Côte d'Azur
styles.style_cote_azur()

# Créer des données
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Tous les graphiques suivants auront le style appliqué
plt.figure(figsize=(10, 6))
plt.plot(x, y1, linewidth=3, label='Vague 1')
plt.plot(x, y2, linewidth=3, label='Vague 2')
plt.fill_between(x, y1, alpha=0.3)

plt.title('🌊 Les Vagues de la Méditerranée')
plt.xlabel('Distance (km)')
plt.ylabel('Amplitude (m)')
plt.legend()
plt.grid(True)
plt.show()

# Restaurer le style par défaut
styles.restaurer_style()
```

**Styles disponibles :**

- `styles.style_versailles()` - 👑 Style royal et élégant avec tons dorés
- `styles.style_bistrot()` - ☕ Ambiance chaleureuse de bistrot parisien
- `styles.style_cote_azur()` - 🌊 Bleus méditerranéens lumineux
- `styles.style_provence()` - 💜 Douceur pastel de la lavande provençale
- `styles.style_parisien()` - 🗼 Élégance minimaliste noir et blanc
- `styles.style_tricolore()` - 🇫🇷 Patriotique aux couleurs du drapeau
- `styles.style_bordeaux()` - 🍷 Rouges profonds des vignobles
- `styles.style_belle_epoque()` - 🎨 Art Nouveau et couleurs organiques
- `styles.restaurer_style()` - Restaure le style matplotlib par défaut

### Mode prétentieux

Transformez vos graphiques en chefs-d'œuvre ridiculement français avec la fonction `rendre_pretentieux()` :

```python
import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib.styles import rendre_pretentieux

# Créer un graphique simple
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

# Rendre le graphique prétentieux ! 🎭
rendre_pretentieux(ax, niveau='modere')  # Options: 'modere', 'insupportable', 'academie_francaise'

plt.tight_layout()
plt.show()
```

**Niveaux de prétention disponibles :**

- `'modere'` - Prétention légère avec formulations élégantes
- `'insupportable'` - Jargon pseudo-scientifique insupportable
- `'academie_francaise'` - Niveau maximal de pédanterie académique

Cette fonction transforme vos titres et labels en versions pompeusement françaises, ajoute des accents circonflexes superflus et des citations prétentieuses. Parfait pour impressionner (ou agacer) vos collègues !

## 🥐 Marqueurs disponibles (tapisseries)

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
- `nuit_parisienne` - Bleu nuit et lumières dorées

### Palettes viticoles

- `bordeaux` - Du rosé au rouge profond
- `champagne` - Pétillant et doré

### Palettes spéciales

- `escargot_persil` - Marron gris-vert
- `french_kiss` - Rouge passionnel
- `je_m_en_fous` - Gris perle élégant

### Palettes humoristiques

- `omelette_ratee` - Du jaune pâle au brun cramé
- `greve_nationale` - Rouge militant et noir protestataire
- `metro_parisien` - Gris métallique, jaune et vert
- `moutarde_dijon` - Jaune moutarde agressif

## 📊 Exemples avancés

### Combinaison style + marqueurs + couleurs

```python
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
```

### Graphique multi-marqueurs

```python
import matplotlib.pyplot as plt
import numpy as np
from frenchplotlib import tapisseries, dorures

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
git clone https://github.com/PhilZPhaZ/frenchplotlib.git
cd frenchplotlib
pip install -e .
```

## 📄 Licence

Ce projet est sous licence MIT.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

- 🐛 Signaler des bugs
- 💡 Proposer de nouvelles fonctionnalités
- 🥐 Ajouter de nouveaux marqueurs ou palettes
- 📚 Améliorer la documentation
- 🎨 Créer de nouveaux styles graphiques

## 🙏 Remerciements

Merci à matplotlib pour son excellente bibliothèque de visualisation qui rend tout cela possible.

---

*Créé avec ❤️ et 🥖 en France*
