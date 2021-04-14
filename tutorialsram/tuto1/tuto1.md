
# Institut des Algorithmes du Sénégal
## _Optimisation sous contrainte_



L’optimisation sous contrainte est un problème que nous rencontrons dans beaucoup de domaines de la vie réelle. Dans ce premier tutoriel, nous utiliserons allo,ns résoudre un probléme d'optimisation avec deux approches :  

- Avec une librairie externe
- Avec l’algorithme Arrow-Hurwicz qu’il faudra implémenter. 

Puis comparrer les résultats obtenus avec les deux approches

Le langage Python inclut des modules qui permettent de résoudre des problèmes d’optimisation sous contraintes et il n’est pas forcément nécessaire de connaître la théorie derrière les algorithmes de résolution pour s’en servir. Au cours de cette séance, on verra comment faire. Même si comprendre comment utiliser une fonction d’un module tel que cvxopt requiert parfois un peu de temps et de lecture.


## Optimisation avec cvxopt

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;min_{xy}={x^2+x^2+y^2-xy+y}) 
sous la contrainte x+2y=1

La librarie cvxopt est un des outils les plus utilisés pour résoudre ce problème. 
Ci-dessous quelques exemples :
```ruby
from cvxopt import solvers, matrix
m = matrix( [ [2.0, 1.1] ] )  # mettre des réels (float) et non des entiers
                              # cvxopt ne fait pas de conversion implicite
t = m.T                       # la transposée
t.size                        # affiche les dimensions de la matrice

```

La documentation cvxopt est parfois peu explicite. Il ne faut pas hésiter à regarder les exemples d’abord et à la lire avec attention les lignes qui décrivent les valeurs que doivent prendre chaque paramètre de la fonction. Le plus intéressant pour le cas qui nous intéresse est celui-ci (tiré de la page problems with nonlinear objectives) :

```ruby
from cvxopt import solvers, matrix, spdiag, log

def acent(A, b):
    m, n = A.size
    def F(x=None, z=None):
        if x is None:
            # l'algorithme fonctionne de manière itérative
            # il faut choisir un x initial, c'est ce qu'on fait ici
            return 0, matrix(1.0, (n,1))
        if min(x) <= 0.0:
            return None   # cas impossible

        # ici commence le code qui définit ce qu'est une itération
        f = -sum(log(x))
        Df = -(x**-1).T
        if z is None: return f, Df
        H = spdiag(z[0] * x**(-2))
        return f, Df, H

    return solvers.cp(F, A=A, b=b)['x']

A = matrix ( [[1.0,2.0]] ).T
b = matrix ( [[ 1.0 ]] )
print(acent(A,b))
```
