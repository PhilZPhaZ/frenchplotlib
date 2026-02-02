from matplotlib.colors import LinearSegmentedColormap, ListedColormap

# Dorure du pain (blanc crème -> doré -> brun)
pain_dore = LinearSegmentedColormap.from_list('pain_dore', ['#F5E6D3', '#F4D9A6', '#E8B870', '#D4974B', '#B87333', '#8B4513'])

# baguette bien cuite (du clair au foncé)
baguette_bien_cuite = LinearSegmentedColormap.from_list('baguette_bien_cuite', ['#FFF5E1', '#FAD6A5', '#E8B870', '#C68642', '#8B4513', '#5C3317'])

# escargot sauce persil (maron gris-vert)
escargot_persil = LinearSegmentedColormap.from_list('escargot_persil', ['#8B7355', '#A0826D', '#6B8E23', '#556B2F'])

# french kiss (rouge passionnel)
french_kiss = LinearSegmentedColormap.from_list('french_kiss', ['#FFB6C1', '#FF69B4', '#FF1493', '#C71585', '#8B0000'])

# je m'en fous (gris perle élégant)
je_m_en_fous = LinearSegmentedColormap.from_list('je_m_en_fous', ['#F0F0F0', '#D3D3D3', '#A9A9A9', '#808080', '#505050'])

# croissant beuréé (or brillant et miel)
croissant_beurre = LinearSegmentedColormap.from_list('croissant_beurre', ['#FFF8DC', '#FFD700', '#FFA500', '#FF8C00', '#DAA520'])

# Tricolore (drapeau français)
tricolore = LinearSegmentedColormap.from_list('tricolore', ['#0055A4', '#FFFFFF', '#EF4135'])

# Lavande de Provence
lavande = LinearSegmentedColormap.from_list('lavande', ['#E6E6FA', '#9B88C4', '#7B68EE', '#6A5ACD', '#483D8B'])

# Bordeaux (vin rouge)
bordeaux = LinearSegmentedColormap.from_list('bordeaux', ['#FFF5F5', '#FFB6C1', '#DC143C', '#8B0000', '#4B0000'])

# Champagne (pétillant et doré)
champagne = LinearSegmentedColormap.from_list('champagne', ['#F0F0E8', '#F5DEB3', '#FFD700', '#DAA520', '#B8860B'])

# Fromage (palette des fromages français)
fromage = LinearSegmentedColormap.from_list('fromage', ['#FFFEF0', '#FFF8DC', '#F5DEB3', '#EAD5A8', '#D4AF37'])

# Côte d'Azur (mer et ciel)
cote_azur = LinearSegmentedColormap.from_list('cote_azur', ['#001F3F', '#0074D9', '#7FDBFF', '#39CCCC', '#3D9970'])

# Automne en Bourgogne
bourgogne = LinearSegmentedColormap.from_list('bourgogne', ['#8B4513', '#A0522D', '#CD853F', '#DEB887', '#F4A460', '#FFD700'])

# Macaron parisien (pastel gourmand)
macaron = ListedColormap(['#FFE4E1', '#FFB6C1', '#DDA0DD', '#B0E0E6', '#98FB98', '#FFFFE0'], name='macaron')

# Versailles (or et royal)
versailles = LinearSegmentedColormap.from_list('versailles', ['#FFF8DC', '#FFD700', '#DAA520', '#B8860B', '#8B7355', '#654321'])

# Nuit parisienne (bleu nuit et lumières dorées)
nuit_parisienne = LinearSegmentedColormap.from_list('nuit_parisienne', ['#000033', '#000066', '#000099', '#3333FF', '#FFFF00', '#FFD700'])
