
# Institut-des-Algorithmes-du-S-n-gal
Institut des Algorithmes du Sénégal




# Simulating COVID-19 interventions with R


## 1. Three representations of an SIR model:

- A verbal description
- A graphical description
- A mathematical description

# 2. Solving differential equations in R

 - Step 1: writing the differential equations in R
 - Step 2: defining some values for the parameters
 - Step 3: defining initial values for the variables
 - Step 4: the points in time where to calculate variables values
 - Step 5: numerically solving the SIR model

# 3. Exercises

- Writing a simulator
- Comparing a model’s predictions with data

# 4. Estimating model’s parameters

- Sums of squares

# 5. Exercises

- Sum of squares profile
- Optimisation
- Estimating R0


# 6. Maximum likelihood estimation with the bbmle package

- Poisson distribution of errors
- Foobar is a Python library for dealing with word pluralization.



###############################Let's go !!!#############################################

# 1. Three representations of an SIR model:


![alt text](https://upload.wikimedia.org/wikipedia/commons/e/e5/SIR_with_carrier_model.png)

The SIR model is a simple mathematical model of epidemics. An epidemic is when the number of people infected with a disease is increasing in a population.

S, I, and R stand for:

S - susceptible. These are people that are not infected with the disease yet. However, they are not immune to it either, and so they can become infected with the disease in the future.
I - infected or infectious. These are people that are infected with the disease and can transmit the disease to susceptible people.
R - recovered. These are people who have recovered from the disease and are immune, so they can no longer be infected with the disease.

![alt text](http://agilevisualization.com/AgileVisualization/EpidemiologicalModels/figures/equation1.png)



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


