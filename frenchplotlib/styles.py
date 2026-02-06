import matplotlib.pyplot as plt
from matplotlib import cycler
import matplotlib as mpl


def style_versailles():
    """
    Style royal et élégant inspiré du château de Versailles
    - Fond crème/ivoire
    - Couleurs or et royales
    - Grille dorée subtile
    """
    plt.style.use('default')
    
    # Couleurs inspirées de Versailles
    colors = ['#D4AF37', '#8B7355', '#FFD700', '#B8860B', '#2E4057', '#9B1B30']
    
    # Configuration
    plt.rcParams['figure.facecolor'] = '#FFF8DC'
    plt.rcParams['axes.facecolor'] = '#FFFEF0'
    plt.rcParams['axes.edgecolor'] = '#D4AF37'
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.prop_cycle'] = cycler('color', colors)
    plt.rcParams['grid.color'] = '#D4AF37'
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['xtick.color'] = '#654321'
    plt.rcParams['ytick.color'] = '#654321'
    plt.rcParams['text.color'] = '#654321'
    plt.rcParams['axes.labelcolor'] = '#654321'
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.titleweight'] = 'bold'
    

def style_bistrot():
    """
    Style rustique et chaleureux d'un bistrot parisien
    - Tons chauds et terreux
    - Ambiance conviviale
    """
    plt.style.use('default')
    
    # Couleurs du bistrot
    colors = ['#8B4513', '#A0522D', '#CD853F', '#DEB887', '#9B1B30', '#2C3E50']
    
    plt.rcParams['figure.facecolor'] = '#F5E6D3'
    plt.rcParams['axes.facecolor'] = '#FFF5E1'
    plt.rcParams['axes.edgecolor'] = '#8B4513'
    plt.rcParams['axes.linewidth'] = 2.5
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.prop_cycle'] = cycler('color', colors)
    plt.rcParams['grid.color'] = '#8B4513'
    plt.rcParams['grid.alpha'] = 0.2
    plt.rcParams['grid.linestyle'] = ':'
    plt.rcParams['xtick.color'] = '#5C3317'
    plt.rcParams['ytick.color'] = '#5C3317'
    plt.rcParams['text.color'] = '#5C3317'
    plt.rcParams['axes.labelcolor'] = '#5C3317'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.titleweight'] = 'bold'


def style_cote_azur():
    """
    Style méditerranéen inspiré de la Côte d'Azur
    - Bleus de la mer et du ciel
    - Tons aquatiques et lumineux
    """
    plt.style.use('default')
    
    # Couleurs de la Méditerranée
    colors = ['#0074D9', '#7FDBFF', '#39CCCC', '#3D9970', '#001F3F', '#FF851B']
    
    plt.rcParams['figure.facecolor'] = '#E6F3FF'
    plt.rcParams['axes.facecolor'] = '#F0F8FF'
    plt.rcParams['axes.edgecolor'] = '#0074D9'
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.prop_cycle'] = cycler('color', colors)
    plt.rcParams['grid.color'] = '#7FDBFF'
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '-'
    plt.rcParams['xtick.color'] = '#001F3F'
    plt.rcParams['ytick.color'] = '#001F3F'
    plt.rcParams['text.color'] = '#001F3F'
    plt.rcParams['axes.labelcolor'] = '#001F3F'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 14


def style_provence():
    """
    Style doux et pastoral inspiré de la Provence
    - Lavandes et tons pastel
    - Ambiance champêtre
    """
    plt.style.use('default')
    
    # Couleurs de Provence
    colors = ['#9B88C4', '#7B68EE', '#E6E6FA', '#DDA0DD', '#556B2F', '#FFD700']
    
    plt.rcParams['figure.facecolor'] = '#F5F0FF'
    plt.rcParams['axes.facecolor'] = '#FAF8FF'
    plt.rcParams['axes.edgecolor'] = '#9B88C4'
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.prop_cycle'] = cycler('color', colors)
    plt.rcParams['grid.color'] = '#E6E6FA'
    plt.rcParams['grid.alpha'] = 0.5
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['xtick.color'] = '#483D8B'
    plt.rcParams['ytick.color'] = '#483D8B'
    plt.rcParams['text.color'] = '#483D8B'
    plt.rcParams['axes.labelcolor'] = '#483D8B'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 14


def style_parisien():
    """
    Style chic et moderne d'un café parisien
    - Noir, blanc et touches dorées
    - Élégance minimaliste
    """
    plt.style.use('default')
    
    # Palette parisienne chic
    colors = ['#2C3E50', '#34495E', '#95A5A6', '#D4AF37', '#C0392B', '#E74C3C']
    
    plt.rcParams['figure.facecolor'] = '#FFFFFF'
    plt.rcParams['axes.facecolor'] = '#FAFAFA'
    plt.rcParams['axes.edgecolor'] = '#2C3E50'
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.prop_cycle'] = cycler('color', colors)
    plt.rcParams['grid.color'] = '#BDC3C7'
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '-'
    plt.rcParams['xtick.color'] = '#2C3E50'
    plt.rcParams['ytick.color'] = '#2C3E50'
    plt.rcParams['text.color'] = '#2C3E50'
    plt.rcParams['axes.labelcolor'] = '#2C3E50'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 15
    plt.rcParams['axes.titleweight'] = 'normal'


def style_tricolore():
    """
    Style patriotique aux couleurs du drapeau français
    - Bleu, blanc, rouge
    - Sobre et élégant
    """
    plt.style.use('default')
    
    # Couleurs du drapeau
    colors = ['#0055A4', '#EF4135', '#FFFFFF', '#002395', '#ED2939', '#87CEEB']
    
    plt.rcParams['figure.facecolor'] = '#F8F9FA'
    plt.rcParams['axes.facecolor'] = '#FFFFFF'
    plt.rcParams['axes.edgecolor'] = '#0055A4'
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.prop_cycle'] = cycler('color', colors)
    plt.rcParams['grid.color'] = '#BDC3C7'
    plt.rcParams['grid.alpha'] = 0.25
    plt.rcParams['grid.linestyle'] = '--'
    plt.rcParams['xtick.color'] = '#2C3E50'
    plt.rcParams['ytick.color'] = '#2C3E50'
    plt.rcParams['text.color'] = '#2C3E50'
    plt.rcParams['axes.labelcolor'] = '#2C3E50'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 14


def style_bordeaux():
    """
    Style élégant inspiré des vignobles de Bordeaux
    - Rouges profonds et tons vineyx
    - Ambiance chaleureuse et raffinée
    """
    plt.style.use('default')
    
    # Couleurs du vin
    colors = ['#8B0000', '#A52A2A', '#DC143C', '#800020', '#722F37', '#B8860B']
    
    plt.rcParams['figure.facecolor'] = '#FFF5F5'
    plt.rcParams['axes.facecolor'] = '#FFFAFA'
    plt.rcParams['axes.edgecolor'] = '#8B0000'
    plt.rcParams['axes.linewidth'] = 2
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.prop_cycle'] = cycler('color', colors)
    plt.rcParams['grid.color'] = '#CD5C5C'
    plt.rcParams['grid.alpha'] = 0.25
    plt.rcParams['grid.linestyle'] = ':'
    plt.rcParams['xtick.color'] = '#4B0000'
    plt.rcParams['ytick.color'] = '#4B0000'
    plt.rcParams['text.color'] = '#4B0000'
    plt.rcParams['axes.labelcolor'] = '#4B0000'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 14


def style_belle_epoque():
    """
    Style Art Nouveau inspiré de la Belle Époque
    - Couleurs organiques et florales
    - Touches dorées et pastel
    """
    plt.style.use('default')
    
    # Palette Belle Époque
    colors = ['#2E4057', '#D4A574', '#8D6E63', '#C9A66B', '#A0522D', '#556B2F']
    
    plt.rcParams['figure.facecolor'] = '#FAF0E6'
    plt.rcParams['axes.facecolor'] = '#FFF8F0'
    plt.rcParams['axes.edgecolor'] = '#8D6E63'
    plt.rcParams['axes.linewidth'] = 2.5
    plt.rcParams['axes.grid'] = True
    plt.rcParams['axes.prop_cycle'] = cycler('color', colors)
    plt.rcParams['grid.color'] = '#D4A574'
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.linestyle'] = '-.'
    plt.rcParams['xtick.color'] = '#5D4037'
    plt.rcParams['ytick.color'] = '#5D4037'
    plt.rcParams['text.color'] = '#5D4037'
    plt.rcParams['axes.labelcolor'] = '#5D4037'
    plt.rcParams['font.size'] = 11
    plt.rcParams['axes.titlesize'] = 15
    plt.rcParams['axes.titleweight'] = 'bold'


def rendre_pretentieux(ax=None, niveau='modere'):
    """
    Transforme un graphique en version prétentieuse à la française
    
    Ajoute des accents circonflexes superflus, des formulations ampoulées
    et un air de supériorité culturelle typiquement français.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes, optional
        Les axes à rendre prétentieux. Si None, utilise les axes courants.
    niveau : str, optional
        Niveau de prétention : 'modere', 'insupportable', ou 'academie_francaise'
        Par défaut 'modere'
        
    Returns
    -------
    ax : matplotlib.axes.Axes
        Les axes transformés
        
    """
    if ax is None:
        ax = plt.gca()
    
    # Dictionnaires de transformation selon le niveau
    transformations_moderees = {
        'graph': 'représentation graphique',
        'plot': 'tracé illustratif',
        'data': 'données empiriques',
        'value': 'valeur numérique',
        'point': 'coordonnée cartésienne',
        'line': 'courbe fonctionnelle',
        'scatter': 'nuage de points discriminants',
        'bar': 'diagramme en bâtonnets',
        'time': 'dimension temporelle',
        'error': 'marge d\'incertitude',
    }
    
    transformations_insupportables = {
        'graph': 'œuvre visuelle analytique',
        'plot': 'représentation esthético-scientifique',
        'data': 'corpus statistique empiriquement validé',
        'value': 'magnitude quantitative certifiée',
        'point': 'entité géométrique bidimensionnelle',
        'line': 'fonction continue différentiable',
        'scatter': 'distribution stochastique de coordonnées',
        'bar': 'histogramme à barres juxtaposées',
        'time': 'continuum spatio-temporel',
        'error': 'intervalle de confiance probabiliste',
    }
    
    transformations_academie = {
        'graph': 'œuvre graphique d\'inspiration cartésienne',
        'plot': 'représentation visuelle de nature épistémologique',
        'data': 'ensemble de données recueillies selon une méthodologie rigoureuse',
        'value': 'grandeur numérique établie conformément aux standards académiques',
        'point': 'élément constitutif d\'un espace vectoriel euclidien',
        'line': 'manifestation géométrique d\'une relation fonctionnelle',
        'scatter': 'constellation de points représentatifs d\'une distribution statistique',
        'bar': 'diagramme en colonnes verticales de hauteurs proportionnelles',
        'time': 'progression chronologique irréversible',
        'error': 'marge d\'erreur inhérente aux limitations méthodologiques',
    }
    
    # Sélection du dictionnaire selon le niveau
    if niveau == 'academie_francaise':
        transfo = transformations_academie
        prefix = "Considérations sur "
        suffix = " (avec toute la rigueur qui s'impose)"
    elif niveau == 'insupportable':
        transfo = transformations_insupportables
        prefix = "Étude approfondie de "
        suffix = " (analyse critique)"
    else:  # modere
        transfo = transformations_moderees
        prefix = "Analyse de "
        suffix = ""
    
    # Transformer le titre
    title = ax.get_title()
    if title:
        # Ajouter des accents circonflexes aléatoires
        title_pretentieux = title.replace('a', 'â').replace('e', 'ê').replace('o', 'ô')
        # Forcer la première lettre en majuscule
        title_pretentieux = prefix + title_pretentieux.capitalize() + suffix
        ax.set_title(title_pretentieux, fontsize=14, fontweight='bold', style='italic')
    else:
        ax.set_title(prefix + "lâ Représentâtion Grâphique" + suffix, 
                    fontsize=14, fontweight='bold', style='italic')
    
    # Transformer les labels des axes
    xlabel = ax.get_xlabel()
    ylabel = ax.get_ylabel()
    
    if xlabel:
        xlabel_pretentieux = xlabel.replace('x', 'χ').replace('X', 'Χ')
        # Chercher des mots communs à remplacer
        for simple, pretentieux in transfo.items():
            if simple.lower() in xlabel.lower():
                xlabel_pretentieux = pretentieux.capitalize()
                break
        ax.set_xlabel(f"Axe des {xlabel_pretentieux}", fontsize=11, style='italic')
    else:
        ax.set_xlabel("Axe des âbscisses (dimension horizontâle)", fontsize=11, style='italic')
    
    if ylabel:
        ylabel_pretentieux = ylabel.replace('y', 'ψ').replace('Y', 'Ψ')
        for simple, pretentieux in transfo.items():
            if simple.lower() in ylabel.lower():
                ylabel_pretentieux = pretentieux.capitalize()
                break
        ax.set_ylabel(f"Axe des {ylabel_pretentieux}", fontsize=11, style='italic')
    else:
        ax.set_ylabel("Axe des ordonnées (dimension verticâle)", fontsize=11, style='italic')
    
    # Ajouter une note de bas de graphique prétentieuse
    citations = [
        "« Tel Descartes l'eût conçu »",
        "« Dans la plus pure tradition française »",
        "« Avec l'élégance qui caractérise notre culture »",
        "« Conformément aux standards académiques »",
        "« Selon les principes de l'École Polytechnique »",
    ]
    
    import random
    citation = random.choice(citations)
    
    ax.text(0.98, 0.02, citation, 
            transform=ax.transAxes,
            fontsize=8, style='italic', 
            ha='right', va='bottom',
            alpha=0.6)
    
    # Modifier la grille pour la rendre plus "élégante"
    ax.grid(True, linestyle=':', alpha=0.3, color='#2C3E50')
    
    return ax


def restaurer_style():
    """
    Restaure le style matplotlib par défaut
    """
    mpl.rcParams.update(mpl.rcParamsDefault)
    plt.style.use('default')
