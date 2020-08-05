class Node:
	def __init__(self, item):
		self.value = item
		self.next = None

def del_mid_node(node):
	front = node.next
	node.value = front.value
	node.next = front.next
	front.next = None

def print_ll(node):
	i = node
	while i.next != None :
		print(i.value)
		i  = i.next
	return 1

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)


a.next = b
b.next = c
c.next = d
d.next = e


print_ll(a)
print()
del_mid_node(c)
print()
print_ll(a)

