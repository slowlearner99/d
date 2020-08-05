class Node(object):
	def __init__(self,item):
		self.value = item
		self.next = None

def kth_to_last_node(head,k):

	a = head
	b = head

	for i in range(k):
		if not b.next:
			return "List is too short"
		else:
			b = b.next

	while(b!=None):
		a = a.next
		b = b.next

	return a.value




a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)
g = Node(7)
h = Node(8)
i = Node(9)
j = Node(10)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = j

print(kth_to_last_node(a,3))