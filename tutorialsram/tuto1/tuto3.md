
# Institut des Algorithmes du Sénégal
## Programmation Linéaire – Problème Du Sac À Dos_

Probléme de maximisation:

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;Max{F=\sum_{\substack{i=1..10}}x_iv_i})

 sous la contrainte
 
![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{\substack{i=1..10}}x_ip_i\leq20)


L’optimisation est un probléme qui consiste à trouver le minimum d’une fonction objectif qui décrit mathématiquement une situation. La programmation linéaire n’est rien de plus que de l’optimisation sur des fonctions objectifs décrites par les équations linéaires. Dans ce tutoriel nous verrons comment résoudre un problème d’optimisation linéaire. À travers, le très célèbre problème du sac à dos que nous résoudrons avec un solveur Python. 

# Résolution d'un probléme d'optimisation

La résolution d’un problème d’optimisation se fait en plusieurs étapes :

- Énoncé du problème

Il s’agit de déterminer la quantité à maximiser ou à minimiser.

- Définition des variables

Il faut définir les variables qui interviendront dans les équations (fonction objectif et contraintes). Définir une variable consiste, tout simplement, à indiquer la grandeur du problème qu’elle représente ainsi que les valeurs possibles qu’elle peut prendre.

- Définition de la fonction objectif

Écrire la fonction objectif (fonction à minimiser) sous forme d’équation mathématique à l’aide des variables définies à l’étape précédente.

- Définition des contraintes
Écrire les contraintes du problème sous forme d’équations toujours en utilisant, de façon exclusive, les variables définies plus haut.

- Résoudre le probléme

À cette étape nous avons un système d’équations constitué d’une fonction à minimiser (ou maximiser) et de contraintes. Ces deux éléments faisant intervenir les mêmes variables. Il faut, résoudre ce système en y appliquant l’une des nombreuses méthodes qui existent (Algorithme du simplex, Algorithme de points intérieurs, etc). On peut aussi utiliser un outil d’optimisation implémenté dans une bibliothèque Python telle que Scipy et CVXPY.

# Énoncé du problème

On dispose d’un sac à dos qui peut contenir 20 kg et d’un ensemble d’objet ayant chacun un poids et une valeur.
On veut pouvoir avoir une valeur maximale dans le sac à dos. La valeur dans le sac à dos étant la somme des valeurs de tous les objets qui ont été mis dans le celui-ci.

| Objet                                | Cout                                 | Poids                                |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| 1 | 2 | 5|
| 2 | 3 | 7|
| 3 | 1 | 4 |
| 4 | 5 | 10 |
| 5 | 1 | 10 |
| 6 | 3 | 4 |
| 7 | 5 | 7 |
| 8 | 2 | 3 |
| 9 | 1 | 2 |
| 10 | 6 | 6 |

# Définition des variables

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x_i)
est la variable de décision, elle vaut 1 si l'objet i est choisit, 0 sinon.

La valeur et le poids de l’objet i sont représentées respectivement par 
![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;p_i) et ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;v_i)

# Fonction objectif

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;F=\sum_{\substack{i=1..10}}x_iv_i)


# Définition des contraintes

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{\substack{i=1..10}}x_ip_i\leq20)

il faut prendre en compte la contrainte venant de la définition des variables de décision : 
![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;x_i=0)
ou 1


# Résolution

Pour la résolution de problème nous utiliserons la bibliothèque CVXPY qui sert à la résolution de problèmes d'optimisation.


```ruby
import cvxpy
import numpy as np
 
# Poids limite
POIDS_LIMITE = 20
 
# Les poids et Valeurs
poids = np.array([5,7,4,10,10,4,7,3,2,6])
valeurs = np.array([2,3,1,5,1,3,5,2,1,6])
 
# Variables de décision
decision = cvxpy.Variable(len(poids),boolean=True)
 
# Contrainte de poids total
contrainte_poids = poids*decision <= POIDS_LIMITE
 
# Fonction objectif
fonction_objectif = valeurs*decision
 
# On résout le problème avec CVXPY en précisant sa nature (Maximisation ou Minimisation)
 
# Puis en passant toutes les contraintes en argument dans une liste
probleme_sacados = cvxpy.Problem(cvxpy.Maximize(fonction_objectif),[contrainte_poids])
 
# On précise le solver à utilisé pour résoudre le problème
# GLPK_MI est un solver dédié au problème de programmation linéaire en nombres entiers
probleme_sacados.solve(solver=cvxpy.GLPK_MI)
```
