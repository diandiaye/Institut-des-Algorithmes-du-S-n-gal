
# Institut des Algorithmes du Sénégal

## Régression ridge

Une manière classique de contrer le surapprentissage est de contraindre les paramètres du modèle prédictif à prendre des valeurs "pas trop grandes" (on dit qu'on régularise le modèle).

Dans le cadre de la régression, au lieu d'estimer les paramètres  ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_i)  par minimisation des moindres carrés, on peut chercher à minimiser:

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i=1}^n|y_{data}[i]-a_0-\sum_{j=1}^da_jx{data}[i]^j|^2+\alpha\sum_{j=1}^da_j^2)



où α est un paramètre positif, fixé a priori par l'utilisateur (on parle d'hyperparamètre car α ne fait pas partie des paramètres estimés par minimisation de la fonction précédente).

On voit apparaître un compromis entre l'adéquation aux données (mesurée par la MSE, premier terme de l'expression) et la valeur des paramètres  
![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_j) (qui interviennent par le carré de la norme euclidienne du vecteur des  ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_d). On remarque que la régression linéaire classique correspond au cas particulier α=0.


Notons deux points discutés dans le polycopié:

- le coefficient ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_0). n'est pas inclus dans la régularisation;

- il vaut mieux normaliser les caractéristiques (les composantes des observations) de manière à ce qu'elles varient dans le même intervalle, sinon la régularisation n'aurait pas le même effet sur chacune d'entre elles.


Cette méthode est la régression ridge

L'influence du paramètre α est illustrée par la cellule suivante, dans le cas d'une régression polynomiale.

Remarquez normalize=True, et notez que vous retrouvez bien les valeurs de la régression linéaire classique pour α=0.


```ruby
ridgealpha0 = lm.Ridge(normalize=True,alpha=0)
ridgealpha0.fit(X_data6,Y_data)
print("ridge regression alpha=0")
print(ridgealpha0.intercept_)
print(ridgealpha0.coef_)
Y_pred_ridgealpha0 = ridgealpha0.predict(X6)

ridgealpha01 = lm.Ridge(normalize=True,alpha=0.1)
ridgealpha01.fit(X_data6,Y_data)
print("\nridge regression alpha=0.1")
print(ridgealpha01.intercept_)
print(ridgealpha01.coef_)
Y_pred_ridgealpha01 = ridgealpha01.predict(X6)

ridgealpha1 = lm.Ridge(normalize=True,alpha=1)
ridgealpha1.fit(X_data6,Y_data)
print("\nridge regression alpha=1")
print(ridgealpha1.intercept_)
print(ridgealpha1.coef_)
Y_pred_ridgealpha1 = ridgealpha1.predict(X6)

ridgealpha10 = lm.Ridge(normalize=True,alpha=10)
ridgealpha10.fit(X_data6,Y_data)
print("\nridge regression alpha=10")
print(ridgealpha10.intercept_)
print(ridgealpha10.coef_)
Y_pred_ridgealpha10 = ridgealpha10.predict(X6)

ridgealpha100 = lm.Ridge(normalize=True,alpha=100)
ridgealpha100.fit(X_data6,Y_data)
print("\nridge regression alpha=100")
print(ridgealpha100.intercept_)
print(ridgealpha100.coef_)
Y_pred_ridgealpha100 = ridgealpha100.predict(X6)

plt.figure(figsize=(10,6))
plt.plot(X_data, Y_data,'o')
plt.plot(X, Y_pred_ridgealpha0, '-g')
plt.plot(X, Y_pred_ridgealpha01, '-b')
plt.plot(X, Y_pred_ridgealpha1, '-c')
plt.plot(X, Y_pred_ridgealpha10, '-r')
plt.plot(X, Y_pred_ridgealpha100, '-k')
plt.xlim(0, 130)
plt.ylim(-10, 80)
plt.xlabel("X: vitesse (km/h)")
plt.ylabel("Y: distance d'arrêt (m)")
plt.grid()
plt.title('régression ridge, d=6')
plt.legend(["observations","alpha=0","alpha=0.1","alpha=1","alpha=10","alpha=100"]);
```

Notez que les coefficients ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_j) pour j dans (1,6) diminuent et que ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_0) tend vers la moyenne des ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;Ydata[i]) lorsque α augmente. Il faut maintenant choisir l'hyperparamètre α .




   
La cellule suivante réalise la régression ridge avec sélection de l'hyperparamètre  α  par validation croisée. Ici, on cherche dans une gamme de valeurs de  α  plus large que celle utilisée par défaut: quelle est-elle exactement? Notez qu'on normalise les caractéristiques et qu'on utilise une validation croisée à 5 plis. Après normalisation, il est d'usage de chercher  α  autour de la valeur 1.

```ruby
ridge1 = lm.RidgeCV(normalize=True, alphas=np.logspace(-5, 5, 20), cv=5)
ridge1.fit(X_data,Y_data)
print("ridge regression, polynome degré 1")
print(ridge1.intercept_)
print(ridge1.coef_)
print("alpha sélectionné: %.5f" %ridge1.alpha_)

ridge2 = lm.RidgeCV(normalize=True, alphas=np.logspace(-5, 5, 20), cv=5)
ridge2.fit(X_data2,Y_data)
print("\nridge regression, polynome degré 2")
print(ridge2.intercept_)
print(ridge2.coef_)
print("alpha sélectionné: %.5f" %ridge2.alpha_)

ridge6 = lm.RidgeCV(normalize=True, alphas=np.logspace(-5, 5, 20), cv=5)
ridge6.fit(X_data6,Y_data)
print("\nridge regression, polynome degré 6")
print(ridge6.intercept_)
print(ridge6.coef_)
print("alpha sélectionné: %.5f" %ridge6.alpha_)
```

```ruby
Y_pred_lrr1=ridge1.predict(X)
Y_pred_lrr2=ridge2.predict(X2)
Y_pred_lrr6=ridge6.predict(X6)

plt.figure(figsize=(10,6))
plt.plot(X_data, Y_data,'o')
plt.plot(X, Y_pred_lrr1, '-g')
plt.plot(X, Y_pred_lrr2, '-b')
plt.plot(X, Y_pred_lrr6, '-c')
plt.xlim(0, 130)
plt.ylim(-10, 80)
plt.xlabel("X: vitesse (km/h)")
plt.ylabel("Y: distance d'arrêt (m)")
plt.grid()
plt.title('régression ridge')
plt.legend(["observations","modèle degré 1","modèle degré 2","modèle degré 6"]);
```
