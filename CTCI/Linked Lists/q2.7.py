class Node(object):
	def __init__(self,item):
		self.value = item
		self.next = None

def is_intersect(head1, head2):
	a = head1
	b = head2
	while(head1.next != None):
		head1 = head1.next
	while(head2.next != None):
		head2 = head2.next
	return head1 == head2



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
d.next = i

e.next = f
f.next = g
g.next = h
h.next = i

i.next = j

print(is_intersect(b,e))