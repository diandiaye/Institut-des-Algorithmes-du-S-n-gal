
# Institut des Algorithmes du Sénégal

## Régression ridge

Une manière classique de contrer le surapprentissage est de contraindre les paramètres du modèle prédictif à prendre des valeurs "pas trop grandes" (on dit qu'on régularise le modèle).

Dans le cadre de la régression, au lieu d'estimer les paramètres  ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_i)  par minimisation des moindres carrés, on peut chercher à minimiser:

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i=1}^n|y_{data}[i]-a_0-\sum_{j=1}^d a_jx{data}[i]^j|^2)


\sum_{i=1}^n\left|y_{data}[i]-a_0-\sum_{j=1}^d a_jx{data}[i]^j\right|^2+\alpha\sum_{j=1}^d a_j^2





où  α  est un paramètre positif, fixé a priori par l'utilisateur (on parle d'hyperparamètre car  α  ne fait pas partie des paramètres estimés par minimisation de la fonction précédente).


