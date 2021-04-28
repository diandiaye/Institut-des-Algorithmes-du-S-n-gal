# Algorithmes du plus court chemin

# Algorithme de Dijkstra

On peut faire appel à la fonction dijkstra du sous-module CSGraph pour appliquer l’algorithme de Dijkstra qui sert à résoudre le problème du plus court chemin dans un graphe orienté pondéré par des réels positifs.

La fonction dijkstra retourne :

- dist_matrix qui est la matrice des distances entre les nœuds du graphe.

- predecessors qui est la matrice des prédécesseurs.

Exemple 5 :

Considérons le graphe ci-après :

![i1](https://user-images.githubusercontent.com/41585144/116443678-3bdd2500-a854-11eb-8040-b5a0f38f1996.jpg)

On lui applique l’algorithme de Dijkstra.

  ```ruby
  from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
G = [[0, 1, 2, 0, 0],
[0, 0, 0, 2, 2],
[0, 3, 0, 2, 0],
[0, 0, 0, 0, 4],
[0, 0, 0, 0, 0]]
G_eparse = csr_matrix(G)
dist_matrix, predecessors = dijkstra (csgraph = G_eparse, directed = True,
return_predecessors = True)
print(dist_matrix)
print(predecessors)
  ```
 Résultat de l’exécution :
