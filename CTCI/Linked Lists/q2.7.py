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


def findMergeNode(head1, head2):
    a = head1
    b = head2
    len_a = 0
    len_b = 0
    while(a.next != None):
        a = a.next
        len_a+=1

    while(b.next != None):
        b = b.next
        len_b+=1
    
    if a == b:
        a = head1
        b = head2
        if len_a > len_b:
            temp = len_a - len_b
            for i in range(temp):
                a = a.next
                
        if len_b > len_a:
            temp = len_b - len_a
            for i in range(temp):
                b = b.next
                
        while(a.next != None and b.next!=None):
            if a==b:
                return a.value
            else:
                a = a.next
                b = b.next             
        return a.value
    else:
        return None

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

# print(is_intersect(b,e))
findMergeNode(b, e)
