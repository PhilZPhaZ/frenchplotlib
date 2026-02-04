from svgpathtools import svg2paths
from svgpath2mpl import parse_path
from matplotlib.path import Path as MplPath
import numpy as np

def load_svg_marker(svg_file_path):
    paths, _ = svg2paths(svg_file_path)

    if not paths:
        raise ValueError(f"Aucun path trouvé dans {svg_file_path}")

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

    # Center the shape
    data_vertices -= data_vertices.mean(axis=0)

    return MplPath(data_vertices, data_codes)
