""" 
A Python program to demonstrate the adjacency 
list representation of the graph 
"""
  
# A class to represent the adjacency list of the node 
class AdjNode:
    # 这相当于一个linkedlist
    def __init__(self, data): 
        self.vertex = data 
        self.next = None
  
  
# A class to represent a graph. A graph 
# is the list of the adjacency lists. 
# Size of the array will be the no. of the 
# vertices "V" 
class Graph: 
    def __init__(self, vertices): 
        self.V = vertices # V是一个list 
        self.graph = [None] * self.V # 这个matrix list 是一个list with linkedlist
  
    # Function to add an edge in an undirected graph
    # 这个方程是给 undirected graph 用的
    # 每有一对Node连接， 都会产生两组add
    # example： 0, 1 =>  0->1 and 1->0
    def add_edge(self, src, dest): 
        # Adding the node to the source node
        node = AdjNode(dest) 
        node.next = self.graph[src] 
        self.graph[src] = node 
  
        # Adding the source node to the destination as 
        # it is the undirected graph 
        node = AdjNode(src) 
        node.next = self.graph[dest] 
        self.graph[dest] = node 
  
    # Function to print the graph 
    def print_graph(self): 
        for i in range(self.V): 
            print("Adjacency list of vertex {}\n head".format(i), end="") 
            temp = self.graph[i] 
            while temp: 
                print(" -> {}".format(temp.vertex), end="") 
                temp = temp.next
            print(" \n") 
  
  
# Driver program to the above graph class 
if __name__ == "__main__": 
    V = 5
    graph = Graph(V) 
    graph.add_edge(0, 1) 
    graph.add_edge(0, 4) 
    graph.add_edge(1, 2) 
    graph.add_edge(1, 3) 
    graph.add_edge(1, 4) 
    graph.add_edge(2, 3) 
    graph.add_edge(3, 4) 
  
    graph.print_graph() 
  
# This code is contributed by Kanav Malhotra 
