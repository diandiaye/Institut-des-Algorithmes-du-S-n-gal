
# Institut des Algorithmes du Sénégal

# Implementation of K-Nearest Neighbors from Scratch using Python


# Introduction

If you’re familiar with machine learning and the basic algorithms that are used in the field, then you’ve probably heard of the k-nearest neighbors algorithm, or KNN. This algorithm is one of the more simple techniques used in machine learning. It is a method preferred by many in the industry because of its ease of use and low calculation time.

The k-nearest neighbors (KNN) algorithm is a simple, easy-to-implement supervised machine learning algorithm that can be used to solve both classification and regression problems. Pause! Let us unpack that. It is a model that classifies data points based on the points that are most similar to it. It uses test data to make an “educated guess” on what an unclassified point should be classified as.

# K-Nearest Neighbors Classifier Learning 

Basic Assumption:

- All instances correspond to points in the n-dimensional space where n represents the number of features in any instance.
- The nearest neighbors of an instance are defined in terms of the Euclidean distance.

# The Mathematics Behind KNN

Just like almost everything else, KNN works because of the deeply rooted mathematical theories it uses. When implementing KNN, the first step is to transform data points into feature vectors, or their mathematical value. The algorithm then works by finding the distance between the mathematical values of these points. The most common way to find this distance is the Euclidean distance, as shown below.

![i15](https://user-images.githubusercontent.com/41585144/117339594-35782a00-aea0-11eb-9e3f-d4720b0631b0.png)

KNN runs this formula to compute the distance between each data point and the test data. It then finds the probability of these points being similar to the test data and classifies it based on which points share the highest probabilities.

# Pseudocode:

- Store all training examples.
- Repeat steps 3, 4, and 5 for each test example.
- Find the K number of training examples nearest to the current test example.
- y_pred for current test example =  most common class among K-Nearest training instances.
- Go to step 2.


# Implementation

You can get the dataset used in this implementationfrom https://github.com/diandiaye/Institut-des-Algorithmes-du-S-n-gal/blob/main/tutorialsram/diabetes.csv

The aim of the implementation is to train a Classifier model to predict the presence of diabetes or not for patients with given informations.

```ruby
# Importing usefull libraries
  
import pandas as pd
  
import numpy as np
  
from sklearn.model_selection import train_test_split
  
from scipy.stats import mode
  
from sklearn.neighbors import KNeighborsClassifier
  
# K Nearest Neighbors Classification
  
class K_Nearest_Neighbors_Classifier() : 
      
    def __init__( self, K ) :
          
        self.K = K
          
    # Function to store training set
          
    def fit( self, X_train, Y_train ) :
          
        self.X_train = X_train
          
        self.Y_train = Y_train
          
        # no_of_training_examples, no_of_features
          
        self.m, self.n = X_train.shape
      
    # Function for prediction
          
    def predict( self, X_test ) :
          
        self.X_test = X_test
          
        # no_of_test_examples, no_of_features
          
        self.m_test, self.n = X_test.shape
          
        # initialize Y_predict
          
        Y_predict = np.zeros( self.m_test )
          
        for i in range( self.m_test ) :
              
            x = self.X_test[i]
              
            # find the K nearest neighbors from current test example
              
            neighbors = np.zeros( self.K )
              
            neighbors = self.find_neighbors( x )
              
            # most frequent class in K neighbors
              
            Y_predict[i] = mode( neighbors )[0][0]    
              
        return Y_predict
      
    # Function to find the K nearest neighbors to current test example
            
    def find_neighbors( self, x ) :
          
        # calculate all the euclidean distances between current 
        # test example x and training set X_train
          
        euclidean_distances = np.zeros( self.m )
          
        for i in range( self.m ) :
              
            d = self.euclidean( x, self.X_train[i] )
              
            euclidean_distances[i] = d
          
        # sort Y_train according to euclidean_distance_array and 
        # store into Y_train_sorted
          
        inds = euclidean_distances.argsort()
          
        Y_train_sorted = self.Y_train[inds]
          
        return Y_train_sorted[:self.K]
      
    # Function to calculate euclidean distance
              
    def euclidean( self, x, x_train ) :
          
        return np.sqrt( np.sum( np.square( x - x_train ) ) )
  
# Driver code
  
def main() :
      
    # Importing dataset
      
    df = pd.read_csv( "diabetes.csv" )
  
    X = df.iloc[:,:-1].values
  
    Y = df.iloc[:,-1:].values
      
    # Splitting dataset into train and test set
  
    X_train, X_test, Y_train, Y_test = train_test_split( 
      X, Y, test_size = 1/3, random_state = 0 )
      
    # Model training
      
    model = K_Nearest_Neighbors_Classifier( K = 3 )
      
    model.fit( X_train, Y_train )
      
    model1 = KNeighborsClassifier( n_neighbors = 3 )
      
    model1.fit( X_train, Y_train )
      
    # Prediction on test set
  
    Y_pred = model.predict( X_test )
      
    Y_pred1 = model1.predict( X_test )
      
    # measure performance
      
    correctly_classified = 0
      
    correctly_classified1 = 0
      
    # counter
      
    count = 0
      
    for count in range( np.size( Y_pred ) ) :
          
        if Y_test[count] == Y_pred[count] :
              
            correctly_classified = correctly_classified + 1
          
        if Y_test[count] == Y_pred1[count] :
              
            correctly_classified1 = correctly_classified1 + 1
              
        count = count + 1
          
    print( "Accuracy on test set by our model       :  ", ( 
      correctly_classified / count ) * 100 )
    print( "Accuracy on test set by sklearn model   :  ", ( 
      correctly_classified1 / count ) * 100 )
      
      
if __name__ == "__main__" : 
      
    main()
```
