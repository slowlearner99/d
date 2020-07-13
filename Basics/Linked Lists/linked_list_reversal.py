class Node(object):

	def __init__(self,value):

		self.value = value
		self.nextnode = None


def reverse(head):

	current = head
	previous = None
	nextn = None

	while current:

		nextn = current.nextnode
		current.nextnode = previous
		previous = current
		current = nextn

	return previous



a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print 'Before Reversal: '
print a.value,
print a.nextnode.value,
print b.nextnode.value,
print c.nextnode.value


a = reverse(a)

print 'After Reversal :'
print a.value,
print a.nextnode.value,
print b.nextnode.value,
print c.nextnode.value