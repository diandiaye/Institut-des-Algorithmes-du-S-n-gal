# Institut des Algorithmes du Sénégal

# Maximum flow - Ford-Fulkerson and Edmonds-Karp

# Table of Contents

  - Flow network
 
  - Ford-Fulkerson method
  
  - Edmonds-Karp algorithm
  
  - Implementation

# 1. Flow network

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


# 2. Ford-Fulkerson method

Let's define one more thing. A residual capacity of an directed edge is the capacity minus the flow. It should be noted that if there is a flow along some directed edge  ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;(u,v)),  then the reversed edge has capacity 0 and we can define the flow of it as ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f((v,u))=-f((u,v))). This also defines the residual capacity for all reversed edges. From all these edges we can create a residual network, which is just a network with the same vertices and same edges, but we use the residual capacities as capacities. The Ford-Fulkerson method works as follows. First we set the flow of each edge to zero. Then we look for an augmenting path from s to t. An augmenting path is simple path in the residual graph, i.e. along the edges whose residual capacity is positive. Is such a path is found, then we can add increase the flow along these edges. We keep on searching for augmenting paths and increasing the flow. Once there doesn't exists an augmenting path any more, the flow is maximal.
Let us specify in more detail, what increasing the flow along an augmenting path means. Let C be the smallest residual capacity of the edges in the path. Then we increase the flow in the following way: we update ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f((u,v))~\text{+=}~C) and ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f((v,u))~\text{-=}~C) for every edge (u,v) in the path.

Here is an example to demonstrate the method. We use the same flow network as above. Initially we start with a flow of 0.

![f1](https://user-images.githubusercontent.com/41585144/116946159-bbfef280-ac79-11eb-8802-0556503c0176.png)

We can find the path ![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;-A-B-t) with the residual capacities 7, 5 and 8. Their minimum is 5, therefore we can increase the flow along this path by 5. This gives a flow of 5 for the network.

![f2](https://user-images.githubusercontent.com/41585144/116946457-7262d780-ac7a-11eb-8fb5-303618e2f46d.png)



![f3](https://user-images.githubusercontent.com/41585144/116946377-3fb8df00-ac7a-11eb-8a88-39925c489602.png)



for every edge (u,v), the flow is increased in the following way :

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f((u,v))~\text{+=}~C)

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f((v,u))~\text{-=}~C) 





