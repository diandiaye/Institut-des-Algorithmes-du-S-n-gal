
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
```

- Step 3: Build a dataframe

In this step, you’ll need to capture the dataset (from step 1) in Python. You can accomplish this task using pandas Dataframe:
```ruby
import pandas as pd
candidates = {'gmat': [780,750,690,710,680,730,690,720,740,690,610,690,710,680,770,610,580,650,540,590,620,600,550,550,570,670,660,580,650,660,640,620,660,660,680,650,670,580,590,690],
              'gpa': [4,3.9,3.3,3.7,3.9,3.7,2.3,3.3,3.3,1.7,2.7,3.7,3.7,3.3,3.3,3,2.7,3.7,2.7,2.3,3.3,2,2.3,2.7,3,3.3,3.7,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.3,1.7,3.7],
              'work_experience': [3,4,3,5,4,6,1,4,5,1,3,5,6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6,5,1,2,4,6,5,1,2,1,4,5],
              'admitted': [1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1]
              }

df = pd.DataFrame(candidates,columns= ['gmat', 'gpa','work_experience','admitted'])
print (df)
```

Alternatively, you could import the data into Python from an external file.

- Step 4: Create the logistic regression in Python

Now, set the independent variables (represented as X) and the dependent variable (represented as y):

```ruby
X = df[['gmat', 'gpa','work_experience']]
y = df['admitted']
```
