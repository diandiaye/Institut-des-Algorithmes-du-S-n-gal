
http://yallouz.arie.free.fr/terminale_cours/graphes/graphes.php?page=g3


# Institut des Algorithmes du Sénégal

## PROBLÈMES DE PLUS COURT CHEMIN

La recherche du meilleur itinéraire que ce soit en distance, en temps ou en coût d'un point à un autre peut être modélisée par la recherche du plus court chemin dans un graphe.

# 1 - GRAPHE PONDÉRÉ

# D éfinition :

On appelle graphe pondéré, un graphe (orienté ou non) dont les arêtes ont été affectées d'un nombre appelé poids (ou coût).

Par analogie avec la matrice d'adjacence, on peut définir la matrice des poids ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;P(a_{i,j})) du graphe, dont les coefficients ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_{i,j}) correspondent aux poids des arêtes (ou des arcs dans le cas d'un graphe orienté) :

On note ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;p_{ij}) le poids de l'arête ( ou de l'arc) entre les sommets ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x_i) et ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x_j)

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_{i,j}=0) si i = j

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_{i,j}=\\infty) s'il n'existe pas d'arêtes ( ou d'arc) entre les sommets ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x_i) et ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x_j)

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_{i,j}=p_{ij}) entre les sommets ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x_i) et ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x_j)



 ## Implémentation
 
 
 ```ruby
def affiche_peres(pere,depart,extremite,trajet):
    """
    À partir du dictionnaire des pères de chaque sommet on renvoie
    la liste des sommets du plus court chemin trouvé. Calcul récursif.
    On part de la fin et on remonte vers le départ du chemin.
    
    """
    if extremite == depart:
        return [depart] + trajet
    else:
        return (affiche_peres(pere, depart, pere[extremite], [extremite] + trajet))
 
 ```
 
 
 ```ruby
 def plus_court(graphe,etape,fin,visites,dist,pere,depart):
    """
    Trouve récursivement la plus courte chaine entre debut et fin avec l'algo de Dijkstra
    visites est une liste et dist et pere des dictionnaires 
    graphe  : le graphe étudié                                                               (dictionnaire)
    étape   : le sommet en cours d'étude                                                     (sommet)
    fin     : but du trajet                                                                  (sommet)
    visites : liste des sommets déjà visités                                                 (liste de sommets)
    dist    : dictionnaire meilleure distance actuelle entre départ et les sommets du graphe (dict sommet : int)
    pere    : dictionnaire des pères actuels des sommets correspondant aux meilleurs chemins (dict sommet : sommet)
    depart  : sommet global de départ                                                        (sommet)
    Retourne le couple (longueur mini (int), trajet correspondant (liste sommets)) 
       
    """
    # si on arrive à la fin, on affiche la distance et les peres
    if etape == fin:
       return dist[fin], affiche_peres(pere,depart,fin,[])
    # si c'est la première visite, c'est que l'étape actuelle est le départ : on met dist[etape] à 0
    if  len(visites) == 0 : dist[etape]=0
    # on commence à tester les voisins non visités
    for voisin in graphe[etape]:
        if voisin not in visites:
            # la distance est soit la distance calculée précédemment soit l'infini
            dist_voisin = dist.get(voisin,float('inf'))
            # on calcule la nouvelle distance calculée en passant par l'étape
            candidat_dist = dist[etape] + graphe[etape][voisin]
            # on effectue les changements si cela donne un chemin plus court
            if candidat_dist < dist_voisin:
                dist[voisin] = candidat_dist
                pere[voisin] = etape
    # on a regardé tous les voisins : le noeud entier est visité
    visites.append(etape)
    # on cherche le sommet *non visité* le plus proche du départ
    non_visites = dict((s, dist.get(s,float('inf'))) for s in graphe if s not in visites)
    noeud_plus_proche = min(non_visites, key = non_visites.get)
    # on applique récursivement en prenant comme nouvelle étape le sommet le plus proche 
    return plus_court(graphe,noeud_plus_proche,fin,visites,dist,pere,depart)
 
def dij_rec(graphe,debut,fin):
    return plus_court(graphe,debut,fin,[],{},{},debut)
 ```
 
 ```ruby
 if __name__ == "__main__":
    g3 = {'a': {'d': 2, 'g': 2},
          'b': {'a' : 1}, 
          'c': {'b' : 1, 'f' : 2, 'g' : 3},
          'd': {'g': 4, 's': 7},
          'e': {'a': 5, 'b' : 3, 'c': 2},
          'f': {'d' : 1,'s' : 6},
          'g': {'f' :4},
          's':{}
    }
    l3,c3 = dij_rec(g3,'e','s')
    print('Plus court chemin ex3 : ',c3, ' de longueur :',l3)
    g4 = {'a': {'d': 5, 'e': 7, 'b' : 2},
          'b': {'e' : 4, 'c' : 9},
          'c': {'e' : 4, 'g' : 6},
          'd': {'e': 3, 'f': 5},
          'e': {'f': 3, 'g' : 4},
          'f': {'h' : 5},
          'g': {'h' : 3},
          'h': {}
    }
    l4,c4 = dij_rec(g4,'a','h')
    print('Plus court chemin ex4 : ',c4, ' de longueur :',l4)
 ```
 
 
