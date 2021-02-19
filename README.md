# Institut-des-Algorithmes-du-S-n-gal
Institut des Algorithmes du Sénégal

## Les modèles de regression
https://towardsdatascience.com/introduction-to-machine-learning-algorithms-linear-regression-14c4e325882a

http://www.sthda.com/english/wiki/regression-analysis-essentials-for-machine-learning#:~:text=Regression%20analysis%20consists%20of%20a,function%20of%20the%20x%20variables.


https://medium.com/towards-artificial-intelligence/gradient-descent-algorithm-explained-2fe9da0de9a2

# Gradient descent algorithm

## Index:

- Basic Rules Of Derivation.

- Gradient Descent With One Variable.

- Gradient Descent With Two Variables.

- Gradient Descent For Mean Squared Error Function.

Foobar is a Python library for dealing with word pluralization.

## What is Gradient Descent ? 

Gradient Descent is a machine learning algorithm thzt operates iteratively to find the optimal values for its parameters. It takes into account, defined learning rate, and initial parameter values.

## How does Gradient Descent work ?

- Start with initial valeus.

- calculate cost

- Update values using the update function.

- Return minimized cost for the predifined cost function

## Why do we need Gradient Descent ?

Generaly, to find the optimal values of the parameters, we find a formula that give thme. But the Gradient Descent algorithm finds the values by itself.

## Formula 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;X=X-lr\frac{d}{dX}f(X)" title="\Large X=X-lr\frac{d}{dX}f(X)" />

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
