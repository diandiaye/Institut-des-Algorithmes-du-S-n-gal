
# Institut des Algorithmes du Sénégal

## Evolution d'une population

On note ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;P_t)  la population l’âge t. La probabilité de mourir à la date t+d lorsqu’on a l’âge t correspond à la probabilité de rester en vie à jusqu’à l’âge t+d puis de mourir dans l’année qui suit :

Le taux de mortalité :

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;m_{t+1}=\frac{p_{t+d}}{p_t}\frac{p_{t+d}-p_{t+d+1}}{p_{t+d}) 

L’espérance de vie s’exprime :

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\mathbb{E}(t)=\sum_{d=1}^\infty{dm_{t+d}}=\sum_{d=1}^\infty{d\frac{P_{t+d}}{P_t}}\frac{P_{t+d}-P_{t+d+1}}{P_{t+d}}=\sum_{d=1}^\infty{d\frac{P_{t+d}-P_{t+d+1}}{P_{t}}})




```ruby


```
