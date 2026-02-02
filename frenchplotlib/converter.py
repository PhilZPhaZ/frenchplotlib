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

"""# ajouter dans __init__.py
init_path = os.path.join(current_dir, '__init__.py')
with open(init_path, 'r') as f:
    content = f.read()

# Extraire tous les noms importés depuis breadplotlib
import_line_start = content.find('from .breadplotlib import')
if import_line_start != -1:
    # Trouver la fin de toutes les lignes d'import
    import_end = content.find('\n\n', import_line_start)
    if import_end == -1:
        import_end = content.find('__all__', import_line_start)

    import_section = content[import_line_start:import_end]

    # Extraire tous les noms importés
    imported_names = []
    for line in import_section.split('\n'):
        if 'from .breadplotlib import' in line:
            names = line.replace('from .breadplotlib import', '').strip()
            imported_names.extend([n.strip() for n in names.split(',')])

    # Ajouter le nouveau nom s'il n'existe pas
    if name not in imported_names:
        imported_names.append(name)

    # Reconstruire la ligne d'import
    new_import_line = f"from .breadplotlib import {', '.join(imported_names)}"

    # Remplacer toute la section d'import par une seule ligne
    new_content = content[:import_line_start] + new_import_line + '\n\n' + content[import_end:].lstrip('\n')
else:
    # Si pas d'import existant, créer la première ligne
    new_content = f"from .breadplotlib import {name}\n\n" + content

# Mettre à jour __all__
if f"'{name}'" not in new_content:
    all_start = new_content.find("__all__ = [")
    if all_start != -1:
        all_end = new_content.find(']', all_start)
        new_content = new_content[:all_end] + f", '{name}'" + new_content[all_end:]

with open(init_path, 'w') as f:
    f.write(new_content)"""
