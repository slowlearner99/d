from collections import defaultdict

class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

		##add the edge u to v in a directed graph
	def addEdge(self,start,end):
		self.graph[start].append(end)

	def route_between_nodes(self,start,end):

		visited = [False] *(len(self.graph))
		queue = []
		queue.append(start)
		visited[start] = True

		while queue:

			temp = queue.pop(0)
			for i in self.graph[temp]:
				if i == end:
					print('Route exists between nodes')
					return

				else:
					if visited[i] == False:
						queue.append(i)
						visited[i] = True

		print('There exists no route between nodes')
		return


g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
g.addEdge(4,5)
g.addEdge(5,4)

g.route_between_nodes(0,3)
g.route_between_nodes(0,5)