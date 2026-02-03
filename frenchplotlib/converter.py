from svgpathtools import svg2paths
from svgpath2mpl import parse_path
import os
import numpy as np
from matplotlib.path import Path as MplPath

try:
    from svgpathtools import svg2paths2
except ImportError:
    svg2paths2 = None

name = 'escargot'
path = f'assets/{name}.svg'

# Get the directory where this file is located
current_dir = os.path.dirname(os.path.abspath(__file__))
svg_path = os.path.join(current_dir, path)

if svg2paths2:
    paths, attributes, _svg_attributes = svg2paths2(svg_path)
else:
    paths, attributes = svg2paths(svg_path)

if not paths:
    raise ValueError(f"Aucun path trouvé dans {svg_path}")

# Convertir tous les paths en un seul Path matplotlib
all_vertices = []
all_codes = []
for p in paths:
    mpl_path = parse_path(p.d())
    if mpl_path.vertices.size == 0:
        continue

    vertices = mpl_path.vertices
    codes = mpl_path.codes
    if codes is None:
        codes = np.full(len(vertices), MplPath.LINETO, dtype=np.uint8)
        codes[0] = MplPath.MOVETO
    else:
        codes = codes.copy()
        codes[0] = MplPath.MOVETO

    all_vertices.append(vertices)
    all_codes.append(codes)

data_vertices = np.vstack(all_vertices)
data_codes = np.concatenate(all_codes)

# Centrer la forme
data_vertices -= data_vertices.mean(axis=0)

# Formatter les vertices avec une ligne par élément
vertices_str = "[\n"
for vertex in data_vertices:
    vertices_str += f"        {vertex.tolist()},\n"
vertices_str += "    ]"

# Formatter les codes sur une ligne (ils sont plus courts)
codes_str = str(data_codes.tolist())

sample = f"""
{name} = Path(
    np.array({vertices_str}),
    np.array({codes_str})
)
"""

# ecrire à la fin du fichier breadplotlib.py
breadplotlib_path = os.path.join(current_dir, 'breadplotlib.py')
with open(breadplotlib_path, 'r') as f:
    content = f.read()

# si on a le nom de la variable deja dans le fichier, ne pas l'ajouter
if f'{name} = Path(' not in content:
    with open(breadplotlib_path, 'a') as f:
        # S'assurer qu'il y a exactement un retour à la ligne avant
        if not content.endswith('\n'):
            f.write('\n')
        f.write(sample + '\n')
