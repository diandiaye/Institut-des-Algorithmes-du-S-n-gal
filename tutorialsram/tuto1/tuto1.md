
# Institut des Algorithmes du Sénégal
## _Optimisation sous contrainte_



L’optimisation sous contrainte est un problème que nous rencontrons dans beaucoup de domaines de la vie réelle. Dans ce premier tutoriel, nous allons résoudre un probléme d'optimisation en utilisant 

- La librarielibrairie cvxopt

Nous avons aussi la possibilité d'utiliser d'autres algorithmes et de comparrer les résultats obtenus avec les deux approches.

Le langage Python inclut des modules(solvers) qui permettent de résoudre des problèmes d’optimisation sous contraintes et il n’est pas forcément nécessaire de connaître la théorie derrière les algorithmes de résolution pour s’en servir.

## Optimisation avec cvxopt

Résolution du probléme d'optimisation

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;min_{xy}(\sum_{j=1}^k A_{\alpha_j})) 

sous la contrainte x+2y=1

La librarie cvxopt est un des outils les plus utilisés pour résoudre ce problème. 
Ci-dessous quelques exemples :
```ruby
from cvxopt import solvers, matrix
m = matrix( [ [3.0, 1.1] ] )  # mettre des réels (float) et non des entiers
                              # cvxopt ne fait pas de conversion implicite
t = m.T                       # la transposée
t.size                        # affiche les dimensions de la matrice

```
```ruby
(1, 3)
```

Touvez une documentation compléte de cvxopt ici http://cvxopt.org/documentation/. Il ne faut pas hésiter à regarder les exemples d’abord et à la lire avec attention les lignes qui décrivent les valeurs que doivent prendre chaque paramètre de la fonction. 

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
```ruby
    pcost       dcost       gap    pres   dres
 0:  0.0000e+00  0.0000e+00  1e+00  1e+00  1e+00
 1:  9.9000e-01  4.6251e+00  1e-02  2e+00  7e+01
 2:  3.6389e+00  3.9677e+00  1e-04  1e-01  3e+01
 3:  3.0555e+00  3.3406e+00  1e-06  1e-01  2e+01
 4:  2.5112e+00  2.7758e+00  1e-08  1e-01  8e+00
 5:  2.1118e+00  2.3358e+00  1e-10  1e-01  4e+00
 6:  1.9684e+00  2.1118e+00  1e-12  6e-02  1e+00
 7:  2.0493e+00  2.0796e+00  1e-14  1e-02  1e-01
 8:  2.0790e+00  2.0794e+00  1e-16  2e-04  2e-03
 9:  2.0794e+00  2.0794e+00  1e-18  2e-06  2e-05
10:  2.0794e+00  2.0794e+00  1e-20  2e-08  2e-07
11:  2.0794e+00  2.0794e+00  1e-22  2e-10  2e-09
Optimal solution found.
[ 5.00e-01]
[ 2.50e-01]
```
