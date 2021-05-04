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



for every edge (u,v), 

the flow is increased in the following way :

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f((u,v))~\text{+=}~C)

![\Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}](https://latex.codecogs.com/svg.latex?\Large&space;f((v,u))~\text{-=}~C) 

# 2.1 Implémentation

# Python

```ruby
# Python program for implementation
# of Ford Fulkerson algorithm
from collections import defaultdict

# This class represents a directed graph
# using adjacency matrix representation
class Graph:

	def __init__(self, graph):
		self.graph = graph # residual graph
		self. ROW = len(graph)
		# self.COL = len(gr[0])

	'''Returns true if there is a path from source 's' to sink 't' in
	residual graph. Also fills parent[] to store the path '''

	def BFS(self, s, t, parent):

		# Mark all the vertices as not visited
		visited = [False]*(self.ROW)

		# Create a queue for BFS
		queue = []

		# Mark the source node as visited and enqueue it
		queue.append(s)
		visited[s] = True

		# Standard BFS Loop
		while queue:

			# Dequeue a vertex from queue and print it
			u = queue.pop(0)

			# Get all adjacent vertices of the dequeued vertex u
			# If a adjacent has not been visited, then mark it
			# visited and enqueue it
			for ind, val in enumerate(self.graph[u]):
				if visited[ind] == False and val > 0:
					# If we find a connection to the sink node,
					# then there is no point in BFS anymore
					# We just have to set its parent and can return true
					if ind == t:
						visited[ind] = True
						return True
					queue.append(ind)
					visited[ind] = True
					parent[ind] = u

		# We didn't reach sink in BFS starting
		# from source, so return false
		return False
			
	
	# Returns tne maximum flow from s to t in the given graph
	def FordFulkerson(self, source, sink):

		# This array is filled by BFS and to store path
		parent = [-1]*(self.ROW)

		max_flow = 0 # There is no flow initially

		# Augment the flow while there is path from source to sink
		while self.BFS(source, sink, parent) :

			# Find minimum residual capacity of the edges along the
			# path filled by BFS. Or we can say find the maximum flow
			# through the path found.
			path_flow = float("Inf")
			s = sink
			while(s != source):
				path_flow = min (path_flow, self.graph[parent[s]][s])
				s = parent[s]

			# Add path flow to overall flow
			max_flow += path_flow

			# update residual capacities of the edges and reverse edges
			# along the path
			v = sink
			while(v != source):
				u = parent[v]
				self.graph[u][v] -= path_flow
				self.graph[v][u] += path_flow
				v = parent[v]

		return max_flow


# Create a graph given in the above diagram

graph = [[0, 16, 13, 0, 0, 0],
		[0, 0, 10, 12, 0, 0],
		[0, 4, 0, 0, 14, 0],
		[0, 0, 9, 0, 0, 20],
		[0, 0, 0, 7, 0, 4],
		[0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0; sink = 5

print ("The maximum possible flow is %d " % g.FordFulkerson(source, sink))

# This code is contributed by Neelam Yadav

```

# Java

```ruby
// Java program for implementation of Ford Fulkerson
// algorithm
import java.io.*;
import java.lang.*;
import java.util.*;
import java.util.LinkedList;

class MaxFlow {
	static final int V = 6; // Number of vertices in graph

	/* Returns true if there is a path from source 's' to
	sink 't' in residual graph. Also fills parent[] to
	store the path */
	boolean bfs(int rGraph[][], int s, int t, int parent[])
	{
		// Create a visited array and mark all vertices as
		// not visited
		boolean visited[] = new boolean[V];
		for (int i = 0; i < V; ++i)
			visited[i] = false;

		// Create a queue, enqueue source vertex and mark
		// source vertex as visited
		LinkedList<Integer> queue
			= new LinkedList<Integer>();
		queue.add(s);
		visited[s] = true;
		parent[s] = -1;

		// Standard BFS Loop
		while (queue.size() != 0) {
			int u = queue.poll();

			for (int v = 0; v < V; v++) {
				if (visited[v] == false
					&& rGraph[u][v] > 0) {
					// If we find a connection to the sink
					// node, then there is no point in BFS
					// anymore We just have to set its parent
					// and can return true
					if (v == t) {
						parent[v] = u;
						return true;
					}
					queue.add(v);
					parent[v] = u;
					visited[v] = true;
				}
			}
		}

		// We didn't reach sink in BFS starting from source,
		// so return false
		return false;
	}

	// Returns tne maximum flow from s to t in the given
	// graph
	int fordFulkerson(int graph[][], int s, int t)
	{
		int u, v;

		// Create a residual graph and fill the residual
		// graph with given capacities in the original graph
		// as residual capacities in residual graph

		// Residual graph where rGraph[i][j] indicates
		// residual capacity of edge from i to j (if there
		// is an edge. If rGraph[i][j] is 0, then there is
		// not)
		int rGraph[][] = new int[V][V];

		for (u = 0; u < V; u++)
			for (v = 0; v < V; v++)
				rGraph[u][v] = graph[u][v];

		// This array is filled by BFS and to store path
		int parent[] = new int[V];

		int max_flow = 0; // There is no flow initially

		// Augment the flow while tere is path from source
		// to sink
		while (bfs(rGraph, s, t, parent)) {
			// Find minimum residual capacity of the edhes
			// along the path filled by BFS. Or we can say
			// find the maximum flow through the path found.
			int path_flow = Integer.MAX_VALUE;
			for (v = t; v != s; v = parent[v]) {
				u = parent[v];
				path_flow
					= Math.min(path_flow, rGraph[u][v]);
			}

			// update residual capacities of the edges and
			// reverse edges along the path
			for (v = t; v != s; v = parent[v]) {
				u = parent[v];
				rGraph[u][v] -= path_flow;
				rGraph[v][u] += path_flow;
			}

			// Add path flow to overall flow
			max_flow += path_flow;
		}

		// Return the overall flow
		return max_flow;
	}

	// Driver program to test above functions
	public static void main(String[] args)
		throws java.lang.Exception
	{
		// Let us create a graph shown in the above example
		int graph[][] = new int[][] {
			{ 0, 16, 13, 0, 0, 0 }, { 0, 0, 10, 12, 0, 0 },
			{ 0, 4, 0, 0, 14, 0 }, { 0, 0, 9, 0, 0, 20 },
			{ 0, 0, 0, 7, 0, 4 }, { 0, 0, 0, 0, 0, 0 }
		};
		MaxFlow m = new MaxFlow();

		System.out.println("The maximum possible flow is "
						+ m.fordFulkerson(graph, 0, 5));
	}
}

```

# C++

```ruby
// C++ program for implementation of Ford Fulkerson
// algorithm
#include <iostream>
#include <limits.h>
#include <queue>
#include <string.h>
using namespace std;

// Number of vertices in given graph
#define V 6

/* Returns true if there is a path from source 's' to sink
't' in residual graph. Also fills parent[] to store the
path */
bool bfs(int rGraph[V][V], int s, int t, int parent[])
{
	// Create a visited array and mark all vertices as not
	// visited
	bool visited[V];
	memset(visited, 0, sizeof(visited));

	// Create a queue, enqueue source vertex and mark source
	// vertex as visited
	queue<int> q;
	q.push(s);
	visited[s] = true;
	parent[s] = -1;

	// Standard BFS Loop
	while (!q.empty()) {
		int u = q.front();
		q.pop();

		for (int v = 0; v < V; v++) {
			if (visited[v] == false && rGraph[u][v] > 0) {
				// If we find a connection to the sink node,
				// then there is no point in BFS anymore We
				// just have to set its parent and can return
				// true
				if (v == t) {
					parent[v] = u;
					return true;
				}
				q.push(v);
				parent[v] = u;
				visited[v] = true;
			}
		}
	}

	// We didn't reach sink in BFS starting from source, so
	// return false
	return false;
}

// Returns the maximum flow from s to t in the given graph
int fordFulkerson(int graph[V][V], int s, int t)
{
	int u, v;

	// Create a residual graph and fill the residual graph
	// with given capacities in the original graph as
	// residual capacities in residual graph
	int rGraph[V]
			[V]; // Residual graph where rGraph[i][j]
				// indicates residual capacity of edge
				// from i to j (if there is an edge. If
				// rGraph[i][j] is 0, then there is not)
	for (u = 0; u < V; u++)
		for (v = 0; v < V; v++)
			rGraph[u][v] = graph[u][v];

	int parent[V]; // This array is filled by BFS and to
				// store path

	int max_flow = 0; // There is no flow initially

	// Augment the flow while tere is path from source to
	// sink
	while (bfs(rGraph, s, t, parent)) {
		// Find minimum residual capacity of the edges along
		// the path filled by BFS. Or we can say find the
		// maximum flow through the path found.
		int path_flow = INT_MAX;
		for (v = t; v != s; v = parent[v]) {
			u = parent[v];
			path_flow = min(path_flow, rGraph[u][v]);
		}

		// update residual capacities of the edges and
		// reverse edges along the path
		for (v = t; v != s; v = parent[v]) {
			u = parent[v];
			rGraph[u][v] -= path_flow;
			rGraph[v][u] += path_flow;
		}

		// Add path flow to overall flow
		max_flow += path_flow;
	}

	// Return the overall flow
	return max_flow;
}

// Driver program to test above functions
int main()
{
	// Let us create a graph shown in the above example
	int graph[V][V]
		= { { 0, 16, 13, 0, 0, 0 }, { 0, 0, 10, 12, 0, 0 },
			{ 0, 4, 0, 0, 14, 0 }, { 0, 0, 9, 0, 0, 20 },
			{ 0, 0, 0, 7, 0, 4 }, { 0, 0, 0, 0, 0, 0 } };

	cout << "The maximum possible flow is "
		<< fordFulkerson(graph, 0, 5);

	return 0;
}

```


# References

# ref 1 : https://www.geeksforgeeks.org/ford-fulkerson-algorithm-

# ref 2 : https://cp-algorithms.com/graph/edmonds_karp

# ref 3 : 


