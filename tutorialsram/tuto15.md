
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
