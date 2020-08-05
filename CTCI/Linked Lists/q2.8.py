class Node(object):

	def __init__(self,value):
		self.item = value	
		self.next = None

def cycle_check(node):

	marker1 = node
	marker2 = node

	while marker2 != None and marker2.next != None:
		marker1 = marker1.next
		marker2 = marker2.next.next

		if marker2 == marker1:
			return marker2.item

	return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c



x = Node(4)
y = Node(5)
z = Node(6)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)

x.next = y
y.next = z
z.next = e
e.next = f
f.next = g
g.next = z

print cycle_check(a)
print cycle_check(x)