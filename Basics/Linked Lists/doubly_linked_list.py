class Node(object):

	def __init__(self,item):
		self.value = item
		self.next_node = None
		self.prev_node = None

a = Node(1)
b = Node(2)
c = Node(3)

b.prev_node = a
a.next_node = b

b.next_node = c
c.prev_node = a


