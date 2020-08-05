class Node(object):

	def __init__(self,item):

		self.value = item
		self.next = None

def create_list(head,n):

	marker1 = head
	arr = [3,5,8,5,10,2,1]
	for i in arr:
		temp = Node(i)
		marker1.next = temp
		marker1 = marker1.next

	return head

def print_list(head1):
	#skip sentinel to print
	marker1 = head1.next

	while(marker1!=None):

		print(marker1.value),
		marker1 = marker1.next

def partition1(head1, pivot):
	
	marker1 = head1.next
	headl = Node(0) ##sentinel node
	markerl = headl
	headr = Node(0) ##sentinel node 
	markerr = headr

	while(marker1 != None):

		temp = marker1
		marker1 = marker1.next
		temp.next = None
		
		if temp.value < pivot:

				markerl.next = temp
				markerl = markerl.next

		else:

				markerr.next = temp
				markerr = markerr.next


	##remove sentinels before merge			
	headl = headl.next 
	headr = headr.next

	markerl.next = headr
	head1.next = headl

	return head1


head1 = Node(0) #sentinel node
head1 = create_list(head1,10)

print_list(head1)
pivot  = 5
print '\n'
head1 = partition1(head1,pivot)
print_list(head1)
