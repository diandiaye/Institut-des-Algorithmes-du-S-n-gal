implementation

https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/



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

Imagine a courier service that wants to ship as many widgets as possible from city s to city t. Unfortunately, there is no way to ship widgets directly from ss to tt, so the courier service must ship the widgets using the intermediate cities a, b, c, and d. Particular pairs of cities are connected by flights, which allow the transport of widgets between those cities. This transportation network can be represented by the following directed graph, where nodes represent cities and directed edges represent flights between those cities.



![IyToKdbIQx-snapshot1](https://user-images.githubusercontent.com/41585144/116802007-8938eb00-ab0f-11eb-9f26-e6f88f2dbff5.png)


Obviously, any realistic airplane can't carry an unlimited number of widgets. Therefore, every flight has a maximum number of widgets that it can carry, dependent on the size of its cargo bay. This maximum is called the capacity for that flight. It is a number associated with each edge in the graph above and denotes the maximum number of widgets that can be transported between cities. The graph below is the graph above plus the corresponding capacities. 
For example, the flight from b to c can carry a maximum of 9 widgets, so edge ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\vec{bc}) has capacity 9.

![AC2QUrlnKR-snapshot2](https://user-images.githubusercontent.com/41585144/116802070-272cb580-ab10-11eb-80e8-2510b90800f7.png)


https://brilliant.org/wiki/flow-network/

https://cp-algorithms.com/graph/edmonds_karp.html#toc-tgt-6






two conditions for the existence of a flow:

The flow of an edge cannot exceed the capacity. 

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f(e)\leq{c(e)}) 

And the sum of the incoming flow of a vertex u has to be equal to <br/>
the sum of the outgoing flow of u except in the source and sink vertices. 

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;\sum_{(v,u)\in{E}}f((v,u))=\sum_{(u,v)\in{E}}f((u,v))) 



