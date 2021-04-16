
# Institut des Algorithmes du Sénégal
## Programmation Linéaire – Problème Du Sac À Dos_


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

| Objet | Cout | Poids |
| ------------------ | ------------------ | ------------------ |
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

