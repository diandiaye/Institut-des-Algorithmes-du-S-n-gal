
# Institut des Algorithmes du Sénégal

# Maximum flow - Ford-Fulkerson and Edmonds-Karp

# Table of Contents

  - Flow network
 
  - Ford-Fulkerson method
  
  - Edmonds-Karp algorithm
  
  - Implementation

# Flow network

In graph theory, a flow network (also known as a transportation network) is a directed graph where each edge has a capacity and each edge receives a flow. The amount of flow on an edge cannot exceed the capacity of the edge.

A flow in a flow network is function f, that again assigns each edge e a non-negative integer value, namely the flow. The function has to fulfill the following two conditions:

The firste condition is that the flow of an edge cannot exceed the capacity.

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f(e)\leq{c(e)}) 

THe second one is that the sum of the incoming flow of a vertex u has to be equal to the sum of the outgoing flow of u except in the source and sink vertices.


![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{(v, u)\in E}f((v, u))=\sum_{(u,v)\in{E}}f((u, v))) 


