class Node(object):
	def __init__(self,item):
		self.value = item
		self.next = None

def palindrome_reverse(head1):
	templist = Node(head1.value)
	templist = duplicate_list(head1,templist)
	head2 = reverse(head1)
	marker1 = head1.next
	marker2 = head2.next

	while marker1 != None and marker2 != None:
		if(marker1.value != marker2.value):
			return False
		marker1 = marker1.next
		marker2 = marker2.next
	
	return True

def reverse(head):

	current = head.next
	previous = None
	nextn = None

	while current:

		nextn = current.next
		current.next = previous
		previous = current
		current = nextn

	return previous

def duplicate_list(head1,templist):

	templist = Node(head1.value)
	marker2 = templist
	marker1 = head1.next

	while(marker1!=None):

		temp = Node(marker1.value)
		marker2.next = temp
		marker2 = marker2.next
		marker1 = marker1.next

	return templist

def create_list(head,n):
	marker1 = head

	for i in range(5):
		temp = Node(i)
		marker1.next = temp
		marker1 = marker1.next

	return head

def print_list(head1):

	marker1 = head1.next
	while(marker1!=None):
		print(marker1.value)
		marker1 = marker1.next

def palindrome_stack(head1):
	fast = head1.next
	slow = head1.next

	stack = []

	while(fast!=None and fast.next !=None):
		stack.append(slow.value)
		slow = slow.next
		fast = fast.next.next

	if(fast!=None):
		slow = slow.next

	while(slow!=None):
		top  = stack.pop()
		if(top != slow.value):
			return False
		slow = slow.next

	return True

head1 = Node(0)
head1 = create_list(head1,5)
print(palindrome_reverse(head1))
head1 = Node(0)
head1 = create_list(head1,5)
print(palindrome_stack(head1))
