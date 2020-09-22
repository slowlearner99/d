class Graph:

	def __init__(self,numvertex):
		self.adjmatrix = [[-1]*numvertex for x in range(numvertex)]
		self.numvertex = numvertex
		self.vertices = {} ##map vertex number to vertex
		self.verticeslist = [0]*numvertex ##

	def set_vertex(self,vtx,id):
		if (vtx >=0 and vtx <=self.numvertex):
			self.vertices[id] = vtx
			self.verticeslist[vtx] = id

	def set_edge(self,frm,to,cost=0):
		frm  = self.vertices[frm]
		to = self.vertices[to]
		self.adjmatrix[frm][to] = cost
		self.adjmatrix[to][frm] = cost	

	def get_vertex(self):
		return self.verticeslist

	def get_matrix(self):
		return self.adjmatrix

	def get_edges(self):
		edges = []
		for i in range(self.numvertex):
			for j in range(self.numvertex):
				if(self.adjmatrix[i][j]!=-1):
					edges.append((self.verticeslist[i],self.verticeslist[j],self.adjmatrix[i][j]))
		return edges

G = Graph(6)
G.set_vertex(0,'a')
G.set_vertex(1,'b')
G.set_vertex(2,'c')
G.set_vertex(3,'d')
G.set_vertex(4,'e')
G.set_vertex(5,'f')
G.set_edge('a','e',10)
G.set_edge('a','c',20)
G.set_edge('c','b',30)
G.set_edge('b','e',40)
G.set_edge('e','d',50)
G.set_edge('f','e',60)
print('Vertices of the Graph')
print(G.get_vertex())
print('Edges of a Graph')
print(G.get_edges())
print('Adjacency matrix of a graph')
print(G.get_matrix())