class Node(object):
	def __init__(self,item):
		self.value = item
		self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(1)
e = Node(2)

a.next = b
b.next = c
c.next = d
d.next = e

import collections

def deldup1(node):

 	iter = node
 	d = collections.defaultdict(int)

 	while(iter != None):

 		if(d[iter.value] > 0):

 			delnode(node,iter.value)

 		else:	

 			d[iter.value] += 1 
 		
 		iter = iter.next

def deldup2(node):

 	iter1 = node

 	while(iter1):

 		iter2 = iter1.next

 		while(iter2 != None):

 			if(iter2.value == iter1.value):

 				delnode(node,iter1.value)

 			iter2 = iter2.next

 		iter1 = iter1.next



def printll(node):

	iter = node

	while(iter!=None):

		print iter.value,
		iter = iter.next


def delnode(node, data):

      while node.value is not data:
         node = node.next
      node.value = node.next.value
      node.next = node.next.next 

printll(a)
deldup1(a)
printll(a)

print '/n'
=-p01`-0987aq1	``	 
 a = Node(1)
b = Node(2)
c = Node(3)
d = Node(1)
e = Node(2)

a.next = b
b.next = c
c.next = d
d.next = e

printll(a)
deldup2(a)
printll(a)

# printll(a)
