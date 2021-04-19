
# Institut des Algorithmes du Sénégal

## Régression ridge

Une manière classique de contrer le surapprentissage est de contraindre les paramètres du modèle prédictif à prendre des valeurs "pas trop grandes" (on dit qu'on régularise le modèle).

Dans le cadre de la régression, au lieu d'estimer les paramètres  ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;a_i)  par minimisation des moindres carrés, on peut chercher à minimiser:

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{i=1}^n \left|y_{data}[i] - a_0 - \sum_{j=1}^d a_j x_{data}[i]^j\right|^2 + \alpha \sum_{j=1}^d a_j^2)


