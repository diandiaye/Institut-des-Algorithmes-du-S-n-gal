
     
  ## Institut des Algorithmes du Sénégal
  
  ![Alt text](https://assets.digitalocean.com/articles/alligator/n15.PNG "a title")
  
  
   ```ruby
import numpy as np
c = np.array([3, 4]) # L'usage de vecteurs (tableau 1D) et matrices (tableau 2D) numpy n'est pas obligatoire mais recommandée
                     # Les tableaux 1D numpy ne sont font pas la distinction entre les vecteurs ligne et les vecteurs colonne.
b = np.array([5, 7, 10])
A = np.array([[ 1, 2],
              [-1, 3],
              [ 2, 1]])
print("c = {}".format(c))
print("b = {}".format(b))
print("A =\n{}".format(A))

nbVariables = len(c)
nbContraites = len(A)
indices = [i for i in range(nbVariables)]

# On définit le problème à maximiser
prob1 = pulp.LpProblem("Mon premier problème revu", pulp.LpMaximize)
# Attention, un nouveau problème prob1 a été créé

x = pulp.LpVariable.dicts("x", indices, lowBound=0, cat="Continuous")

# la fonction 'sum' (ou de façon équivalente pulp.lpSum) est très utile 
prob1 += sum(c[i]*x[i] for i in range(nbVariables))

for j in range(nbContraites):
    prob1 += sum(A[j,i] * x[i] for i in range(nbVariables)) <= b[j], "contrainte {}".format(j+1)
    # attention à changer le nom de chaque contrainte sinon on obtient une erreur.
    
# choix du solver
prob1.solve(pulp.GLPK_CMD(msg=1))
print("Statut:", pulp.LpStatus[prob1.status])

# valeur optimale
val_opt = pulp.value(prob1.objective)
print("Fonction objectif optimale = ", val_opt)

# pour récupérer les valeurs de la solution optimale
x_opt = [x[i].varValue for i in range(nbVariables)]
print("x_opt = ", x_opt)
   ```
