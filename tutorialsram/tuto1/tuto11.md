# Algorithmes du plus court chemin

# 1. Algorithme de Dijkstra

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


# 2. Algorithme de Floyd – Warshall

La fonction floyd_warshall permet de calculer les distances des plus courts chemins entre toutes les paires de sommets dans un graphe orienté et pondéré selon l’algorithme Floyd - Warshall.

La fonction floyd_warshall retourne :

- dist_matrix qui est la matrice des distances entre les nœuds du graphe.

- predecessors qui est la matrice des prédécesseurs.

```ruby
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
G = [[0, 1, 2, 0, 0],
[0, 0, 0, 2, 2],
[0, 3, 0, 5, 0],
[0, 0, 0, 0, 6],
[0, 0, 0, 0, 0]]
G_eparse = csr_matrix(G)
dist_matrix, predecessors = floyd_warshall ( csgraph = G_eparse, directed = True,
return_predecessors = True )
print(dist_matrix)
print(predecessors)
```

## Problémee du voyageur de commerce

```ruby
import random
n = 30
x = [ random.random() for _ in range(n) ]
y = [ random.random() for _ in range(n) ]
import matplotlib.pyplot as plt
plt.plot(x,y,"o")
def longueur (x,y, ordre):
    i = ordre[-1]
    x0,y0 = x[i], y[i]
    d = 0
    for o in ordre:
        x1,y1 = x[o], y[o]
        d += (x0-x1)**2 + (y0-y1)**2
        x0,y0 = x1,y1
    return d

ordre = list(range(len(x)))
print("longueur initiale", longueur(x,y,ordre))

def permutation(x,y,ordre):
    d  = longueur(x,y,ordre)
    d0 = d+1
    it = 1
    while d < d0 :
        it += 1
        print("iteration",it, "d=",d, "ordre[0]", ordre[0])
        d0 = d
        for i in range(1,len(ordre)-1) :  # on part de 1 et plus de 0, on est sûr que le premier noeud ne bouge pas
            for j in range(i+2,len(ordre)):
                r = ordre[i:j].copy()
                r.reverse()
                ordre2 = ordre[:i] + r + ordre[j:]
                t = longueur(x,y,ordre2)
                if t < d :
                    d = t
                    ordre = ordre2
    return ordre

ordre = permutation (x,y,list(range(len(x))))
print("longueur min", longueur(x,y,ordre))
xo = [ x[o] for o in ordre + [ordre[0]]]
yo = [ y[o] for o in ordre + [ordre[0]]]
plt.plot(xo,yo, "o-")
plt.text(xo[0],yo[0],"0",color="r",weight="bold",size="x-large")
plt.text(xo[-2],yo[-2],"N-1",color="r",weight="bold",size="x-large")
```
