
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
