class AdjNode:

	def __init__(self,data):
		self.vertex = data
		self.next = None

class Graph:

	def __init__(self,vertices):
		self.V = vertices
		self.graph = [None]*self.V ##Linked List with 'n' None, so initialised linked list 

###Fucntion to add edge in undirected graph 
	def add_edge(self,src,dest):
		##adding node to source node 
		node = AdjNode(dest)
		node.next = self.graph[src]
		self.graph[src] = node
	##adding source node to destination as it is an undirected graph 
		node = AdjNode(src)
		node.next = self.graph[dest]
		self.graph[dest] = node

	def print_graph(self):
		for i in range(self.V):
			print("Adjacency list of vertex {} \n head".format(i), end="")
			temp = self.graph[i]
			while temp:
				print(" -> {}".format(temp.vertex), end="")
				temp = temp.next
			print("\n") 

graph = Graph(5) 
graph.add_edge(0, 1) 
graph.add_edge(0, 4) 
graph.add_edge(1, 2) 
graph.add_edge(1, 3) 
graph.add_edge(1, 4) 
graph.add_edge(2, 3) 
graph.add_edge(3, 4) 
  
graph.print_graph()