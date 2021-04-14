
# Institut des Algorithmes du Sénégal
## _Optimisation sous contrainte_



L’optimisation sous contrainte est un problème que nous rencontrons dans beaucoup de domaines de la vie réelle. Dans ce premier tutoriel, nous allons résoudre un probléme d'optimisation en utilisant 

- La librarielibrairie cvxopt

Nous avons aussi la possibilité d'utiliser d'autres algorithmes et de comparrer les résultats obtenus avec les deux approches.

Le langage Python inclut des modules(solvers) qui permettent de résoudre des problèmes d’optimisation sous contraintes et il n’est pas forcément nécessaire de connaître la théorie derrière les algorithmes de résolution pour s’en servir.

## Optimisation avec cvxopt

Résolution du probléme d'optimisation

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;min_{xy}({x^2+y^2-xy+y})) 

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
from cvxopt import solvers, matrix
import random

def fonction(x=None,z=None) :
    if x is None :
        x0 = matrix ( [[ random.random(), random.random() ]])
        return 0,x0
    f = x[0]**2 + x[1]**2 - x[0]*x[1] + x[1]
    d = matrix ( [ x[0]*2 - x[1], x[1]*2 - x[0] + 1 ] ).T
    if z is None:
        return f, d
    else :
        h = z[0] * matrix ( [ [ 2.0, -1.0], [-1.0, 2.0] ])
        return f, d, h

A = matrix([ [ 1.0, 2.0 ] ]).trans()
b = matrix ( [[ 1.0] ] )

sol = solvers.cp ( fonction, A = A, b = b)
print (sol)
print ("solution:",sol['x'].T)
```
```ruby
     pcost       dcost       gap    pres   dres
 0:  0.0000e+00  4.3222e-01  1e+00  1e+00  1e+00
 1:  2.6022e-01  4.2857e-01  1e-02  1e-01  1e-02
 2:  4.2687e-01  4.2857e-01  1e-04  1e-03  1e-04
 3:  4.2855e-01  4.2857e-01  1e-06  1e-05  1e-06
 4:  4.2857e-01  4.2857e-01  1e-08  1e-07  1e-08
 5:  4.2857e-01  4.2857e-01  1e-10  1e-09  1e-10
Optimal solution found.
{'dual objective': 0.42857142857142855, 'primal objective': 0.4285714268720223, 'primal slack': 1.000000000000004e-10, 'snl': <0x1 matrix, tc='d'>, 'relative gap': 2.333333333333341e-10, 'sl': <0x1 matrix, tc='d'>, 'dual slack': 0.9999999999999991, 'status': 'optimal', 'y': <1x1 matrix, tc='d'>, 'x': <2x1 matrix, tc='d'>, 'zl': <0x1 matrix, tc='d'>, 'znl': <0x1 matrix, tc='d'>, 'dual infeasibility': 9.995026102717158e-11, 'gap': 1.0000000000000031e-10, 'primal infeasibility': 1.2214984990086318e-09}
solution: [ 4.29e-01  2.86e-01]
```
