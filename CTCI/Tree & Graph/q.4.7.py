from collections import defaultdict

class Graph:

	def __init__(self):
		self.vertices = []
		self.graph = defaultdict(list)

	def addEdge(self,start,end):
		self.graph[start].append(end)

	def addVertex(self,vertex):
		self.vertices.append(vertex)
		self.addEdge(vertex,-1)
		self.graph[vertex].remove(-1)

	def buildorder(self,order):
		graphClone = self.graph
		while(len(order) <= len(self.vertices)):
			for vertex in graphClone:
				if graphClone[vertex]==[]:
					if vertex not in order:
						order.append(vertex)
					for edges in graphClone.values():
						if vertex in edges:
							edges.remove(vertex)
		return order

g = Graph()

g.addVertex('a')
g.addVertex('b')
g.addVertex('c')
g.addVertex('d')
g.addVertex('e')
g.addVertex('f')

g.addEdge('a','b')
g.addEdge('a','f')
g.addEdge('a','c')
g.addEdge('b','f')
g.addEdge('c','f')
g.addEdge('e','a')
g.addEdge('e','b')
g.addEdge('g','d')


order = []
print(g.buildorder(order))



