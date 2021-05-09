
# Institut des Algorithmes du Sénégal

#  Logistic Regression in Python

In this tutorial, we’ll show you an example of Logistic Regression in Python.

In general, a binary logistic regression describes the relationship between the dependent binary variable and one or more independent variable/s.

The binary dependent variable has two possible outcomes:


    - ‘1’ for true/success; or
    - ‘0’ for false/failure
Let’s now see how to apply logistic regression in Python using a practical example.

We will Apply different steps to build a Logistic Regression model in Python

- Step 1: Gather your data

To start with a simple example, let’s say that your goal is to build a logistic regression model in Python in order to determine whether candidates would get admitted to a prestigious university.

Here, there are two possible outcomes: Admitted (represented by the value of ‘1’) vs. Rejected (represented by the value of ‘0’).

We can then build a logistic regression in Python, where:

    - The dependent variable represents whether a person gets admitted; and
     -The 3 independent variables are the GMAT score, GPA and Years of work experience


- Step 2: Import the needed Python packages

Before starting, make sure that the following packages are installed in Python environment:

    - pandas – used to create the DataFrame to capture the dataset in Python
    - sklearn – used to build the logistic regression model in Python
    - seaborn – used to create the Confusion Matrix
    - matplotlib – used to display charts

Then you can import all the packages as follows:

```ruby
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt
```r
