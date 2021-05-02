
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


![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{(v,u)\in{E}}f((v,u))=\sum_{(u,v)\in{E}}f((u,v))) 

It is easy to see that the following equation holds:

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{(s,u)\in{E}}f((s,u))=\sum_{(u,t)\in{E}}f((u,t))) 


# Below an exellent illustration of flow use case

Imagine a courier service that wants to ship as many widgets as possible from city ss to city tt. Unfortunately, there is no way to ship widgets directly from ss to tt, so the courier service must ship the widgets using the intermediate cities aa, bb, cc, and dd. Particular pairs of cities are connected by flights, which allow the transport of widgets between those cities. This transportation network can be represented by the following directed graph, where nodes represent cities and directed edges represent flights between those cities.

![i1](![image](https://user-images.githubusercontent.com/41585144/116801995-70c8d080-ab0f-11eb-80e0-230a285cda56.png))




