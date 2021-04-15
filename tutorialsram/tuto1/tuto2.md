
# Institut des Algorithmes du Sénégal


![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;y_j=f(x_j)+e_j\quad)

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f(x)=f(x;c_0,c_1,c_2,\ldots,c_d))

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;=c_0+c_1x+c_2x^2+\ldots+c_dx^d)



## Les méthodes de regression

Dans cette sèrie, nous allons nous intéresser aux problèmes de régression sous l'angle des problématiques de l'apprentissage automatique. Rappelons que les problèmes de régression font partie de l'apprentissage supervisé. 
Vous avez peut-être étudié la régression dans un cours d'analyse de données.
Cette sèrie de tutos sera sectionnée en différentes parties :

nous introduisons à présent la notion de régularisation qui interviendra à plusieurs reprises dans la suite de ce cours.

- Regression linéaire simple
- Régression avec une pénalisation de ridge
- Regression linéaire avec une pénalisation de Lasso
- 
# 1. ression linéaire simple

-Les données : distance de freinage en fonction de la vitesse d'un véhicule

L'objectif de cette première partie est de prédire la distance d'arrêt d'un véhicule en fonction de sa vitesse, en utilisant des données.

vous trouveraient sur ce lien https://github.com/diandiaye/Institut-des-Algorithmes-du-S-n-gal/blob/main/tutorialsram/tuto1/cars.csv les données, vous pouvez les télécharger et nommez-le ficher "vitesse_freinage.csv".

Dans le code ci-dessous, on charge les données que nous allons utiliser pour faire la prédiction.

```ruby
import pandas as pd
data =   pd.read_csv("cars.csv") # On charge les données précédement sauvegardées

print(data)## Afficher les données

# pour utiliser les modules sklearn, il faut que les données soient représentées par des vecteurs colonnes
X_data = data[:,0].reshape(len(data),1)  # première colonne (sans reshape, X_data serait un vecteur ligne)
Y_data = data[:,1].reshape(len(data),1)  # deuxième colonne
print("\nnombre d'observations : %d" %len(X_data))
plt.figure(figsize=(10,6))
plt.scatter(X_data, Y_data)
plt.xlabel("X: vitesse (km/h)")
plt.ylabel("Y: distance d'arrêt (m)")
plt.grid()
plt.xlim(0, 130)
plt.ylim(0, 100);  # le ; permet d'éviter un affichage intempestif dans le carnet
```

Nous allons à présent développer un modèle de regression permettant de prédire les valeurs y correspondant à des valeurs de x entre 0 et 150 km/h.

Le modèle de regression linéaire consiste à prédire les valeurs de y par une fonction affine de x:

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;y_{pred}=c_0+c_1x)

 Les valeurs de c_0 et c_1 sont estimées par la méthode des moindres carrés: on cherche les paramètres a0 et a1 qui minimisent la fonction
 
 

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i=1}^n\left|y_{data}[i]-a_0-a_1x_{data}[i]\right|^2)

# Calcul des valeurs de 
c_0 et c_1 :
```ruby

# On crée un objet scikit-learn pour la régression linéaire:
lr = lm.LinearRegression()
# lorsqu'on crée un objet scikit-learn, on dispose de méthodes et attributs 
# voir les détails dans la documentation de LinearRegression: on ne se servira que de quelques uns d'entre eux

# On estime les paramètres c0 et c1: 
# (remarque: sklearn attend des données sous forme de vecteurs colonnes)
lr.fit(X_data, Y_data)  
# de manière générale, la méthode fit permet l'apprentissage des paramètres du modèle 
# (ici par la méthodes des moindres carrés), qui sont stockés ici dans les attributs suivants:
print(lr.intercept_)  
print(lr.coef_)
```

# La cellule suivante représente graphiquement la prédiction par régression linéaire.

```ruby
# On "prédit" les valeurs de y pour 30 valeurs de x comprises entre 0 et 15
X = np.linspace(0,15,num=30).reshape(30,1)
Y_pred_lr = lr.predict(X)  
# la méthode predict permet de prédire les valeurs y pour les valeurs de x passées en argument
# (à l'aide du modèle lr)

plt.figure(figsize=(10,6))
plt.plot(X_data, Y_data,'o')
plt.plot(X, Y_pred_lr, '-g')
plt.xlim(0, 15)
plt.ylim(-10, 100)
plt.xlabel("X: vitesse (km/h)")
plt.ylabel("Y: distance d'arrêt (m)")
plt.grid()
plt.title('observations et régression linéaire')
plt.legend(["observations","droite de régression"]);
```

