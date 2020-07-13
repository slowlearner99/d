class Node(object):
	def __init__(self,item):
		self.value = item
		self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e


def nth_to_last_node(item,node):

	marker1 = node
	marker2 = node
	for i in range(item):
		if not marker2.next:
			print 'n is greater than the linked list'
		marker2 = marker2.next

	while marker2:
		marker1 = marker1.next
		marker2 = marker2.next

	return marker1;

target_node = nth_to_last_node(2,a)

print target_node.value