# Institut des Algorithmes du Sénégal




# Simulating COVID-19 interventions with R


## 1. Three representations of an SIR model:

- A verbal description
- A graphical description
- A mathematical description

# 2. Solving differential equations in R

 - f1. writing the differential equations in R
 - f2. : defining some values for the parameters
 - f3. : defining initial values for the variables
 - f4. : the points in time where to calculate variables values
 - f5. : numerically solving the SIR model

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
- A graphical description

![alt text](https://upload.wikimedia.org/wikipedia/commons/e/e5/SIR_with_carrier_model.png)

- A verbal description

The SIR model is a simple mathematical model of epidemics. An epidemic is when the number of people infected with a disease is increasing in a population.

S, I, and R stand for:

S - susceptible. These are people that are not infected with the disease yet. However, they are not immune to it either, and so they can become infected with the disease in the future.
I - infected or infectious. These are people that are infected with the disease and can transmit the disease to susceptible people.
R - recovered. These are people who have recovered from the disease and are immune, so they can no longer be infected with the disease.

- A mathmatical description

![alt text](http://agilevisualization.com/AgileVisualization/EpidemiologicalModels/figures/equation1.png)


# 2. Simulating SIR model with R
To solve a system of differential equations we have to find the values of the variables, in this case, we have to find  S I and R at a number of points in time. 
These values will depend on the values of epidemiological parameters. 
For solving numerically differential equations in R we use the ode() function of the deSolve package. 
We have first to install this package on our system : 


```python
install.packages("deSolve")
```

After installation, to be able to use the deSolve package, we need to load it:

```python
library(deSolve)# This makes it possible to use the "ode" function
```

# - f1. writing the differential equations in R

```python
sir <- function(time, variables, parameters) {
  with(as.list(c(variables, parameters)), {
    dS <- -beta * I * S
    dI <-  beta * I * S - gamma * I
    dR <-  gamma * I
    return(list(c(dS, dI, dR)))
  })
}
```

# - f2. Initialize the parameters values


```python
params_val <- c(
  beta  = 0.004, # infectious contact rate (/person/day)
  gamma = 0.5    # recovery rate (/day)
)
```
# f3. Initialize the varibles of the model

```python
initial_variables <- c(
  S = 999,  # number of susceptibles at time = 0
  I =   1,  # number of infectious at time = 0
  R =   0   # number of recovered (and immune) at time = 0
)
```

# f4. Define time value

```python
time_values <- seq(0, 10) # days
```
# f5. Solve numerically the model

Let's combine the values that we defined and the sir equation : 

```python
sir_mode_values <- ode(
  y = initial_variables,
  times = time_values,
  func = sir,
  parms = params_val 
)
```

We can now print the results by using the following command :

```python
sir_values_1
```


# TO BE CONTINUED








