

# Institut des Algorithmes du Sénégal

# Create a Simple Neural Network in Python

Neural networks (NN), also called artificial neural networks (ANN) are a subset of learning algorithms within the machine learning field that are loosely based on the concept of biological neural networks. ( By Dr. Michael J. Garbade).

Basically, an ANN comprises of the following components:

- An input layer that receives data and pass it on
-  A hidden layer
-  An output layer
-  Weights between the layers
-  A deliberate activation function for every hidden layer. In this simple neural network Python tutorial, we’ll employ the Sigmoid activation function.



There are several types of neural networks. In this project, we are going to create the feed-forward or perception neural networks. This type of ANN relays data directly from the front to the back.

Training the feed-forward neurons often need back-propagation, which provides the network with corresponding set of inputs and outputs. When the input data is transmitted into the neuron, it is processed, and an output is generated.

Here is a diagram that shows the structure of a simple neural network:


![n11](https://user-images.githubusercontent.com/41585144/117682635-8dba6f00-b1b3-11eb-9c1d-4baaf7f40086.png)

So in order to understand how neural networks work, in this tutorial, we'll try to build one by our self.


The problem

Here is a table that shows the problem.

![n12](https://user-images.githubusercontent.com/41585144/117683004-ec7fe880-b1b3-11eb-892c-f8946e5b8993.PNG)

In this tutorial, we are going to train the neural network such that it can predict the correct output value when provided with a new set of data.

As you can see on the table, the value of the output is always equal to the first value in the input section. Therefore, we expect the value of the output (?) to be 1.

Let’s see if we can use some Python code to give the same result (You can peruse the code for this project at the end of this article before continuing with the reading).


# Create a NeuralNetwork Class

We’ll create a NeuralNetwork class in Python to train the neuron to give an accurate prediction. The class will also have other helper functions.


ven though we’ll not use a neural network library for this simple neural network example, we’ll import the numpy library to assist with the calculations.

The library comes with the following four important methods:

1. exp—for generating the natural exponential
2. array—for generating a matrix
3. dot—for multiplying matrices
4. random—for generating random numbers. Note that we’ll seed the random numbers to ensure their efficient distribution.


- Applying the Sigmoid function

This function can map any value to a value from 0 to 1. It will assist us to normalize the weighted sum of the inputs.

Thereafter, we’ll create the derivative of the Sigmoid function to help in computing the essential adjustments to the weights.

The output of a Sigmoid function can be employed to generate its derivative. For example, if the output variable is “x”, then its derivative will be x * (1-x).


#  Training the model

```ruby
import numpy as np

class NeuralNetwork():
    
    def __init__(self):
        # seeding for random number generation
        np.random.seed(1)
        
        #converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def sigmoid(self, x):
        #applying the sigmoid function
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        #computing derivative to the Sigmoid function
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iterations):
        
        #training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            #siphon the training data via  the neuron
            output = self.think(training_inputs)

            #computing error rate for back-propagation
            error = training_outputs - output
            
            #performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments

    def think(self, inputs):
        #passing the inputs via the neuron to get output   
        #converting values to floats
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


if __name__ == "__main__":

    #initializing the neuron class
    neural_network = NeuralNetwork()

    print("Beginning Randomly Generated Weights: ")
    print(neural_network.synaptic_weights)

    #training data consisting of 4 examples--3 input values and 1 output
    training_inputs = np.array([[0,0,1],
                                [1,1,1],
                                [1,0,1],
                                [0,1,1]])

    training_outputs = np.array([[0,1,1,0]]).T

    #training taking place
    neural_network.train(training_inputs, training_outputs, 15000)

    print("Ending Weights After Training: ")
    print(neural_network.synaptic_weights)

    user_input_one = str(input("User Input One: "))
    user_input_two = str(input("User Input Two: "))
    user_input_three = str(input("User Input Three: "))
    
    print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
    print("New Output data: ")
    print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))
    print("Wow, we did it!")
    ```
