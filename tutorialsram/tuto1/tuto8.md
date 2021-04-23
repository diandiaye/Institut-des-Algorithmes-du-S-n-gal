## Institut des Algorithmes du Sénégal

## Le principe du “diviser pour régner” en Python

On souhaite calculer ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;N=7^{52}). La méthode basique consiste à multiplier le nombre 7 par lui-même 52 fois… Ce qui n’est pas très rapide !

L’idée consiste donc à diviser le problème en 2 : on va calculer ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;7^{26}\times7^{26}), c’est-à-dire ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;(7^{26})^2). Là, il n’y a plus que 26 + 1 opérations (26 multiplications pour calculer ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;7^{26}), et une dernière pour faire le carré du résultat.

On recommence ensuite avec ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;7^{26}) : on le calcule en faisant ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;(7^{13})^2). N se calcule alors en 13+1+1 opérations au lieu de 52 initialement.

## Implémentation en Python du “diviser pour régner”

```ruby
def puissance(x,n):
    if n == 0:
        return 1
    elif n%2 == 0:
        return puissance(x*x , n/2)
    else:
        return x * puissance(x*x , (n-1)/2)
    
print(puissance(4,10))
```



