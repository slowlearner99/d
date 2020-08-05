class Node(object):
	def __init__(self,item):
		self.value = item
		self.next = None

def print_list(head1):
	marker1 = head1.next
	while(marker1!=None):
		print(marker1.value)
		marker1 = marker1.next

def get_length(head1):
	llength = 0
	marker1 = head1
	while(marker1!= None):
		llength += 1
		marker1 = marker1.next
	return llength

def pad(head1,n):
	if n < 1:
		return head1
	else: 
		for i in range(n):
			temp = Node(0)
			temp.next = head1
			head1 = temp

		return head1 

def create_list(head,n,list):
	marker1 = head

	for i in list:

		temp = Node(i)
		marker1.next = temp
		marker1 = marker1.next

	return head

def addremainder(head1,pos,remainder):

	marker1 = head1.next
	while(pos>0):
		marker1 = marker1.next
		pos -=1
	marker1.value += remainder

	return head1

def sum_list2(head1,head2,head3):
	remainder = 0
	a = get_length(head1)
	b = get_length(head2)
	pos = 1
	marker1 = head1.next
	marker2 = head2.next
	marker3 = head3

	if (a > b):
		pad(head2,a-b)

	else:
		pad(head2,b-a)
		
	while(marker1 !=None and marker2 != None):

	 	sum = (marker1.value+marker2.value)%10
	 	remainder = (marker1.value + marker2.value)//10

	 	temp = Node(sum)
	 	marker3.next = temp
	 	marker3 = marker3.next

	 	if(remainder > 0):
	 		head3 = addremainder(head3,pos-1,remainder)

	 	pos += 1
	 	marker1 = marker1.next
	 	marker2 = marker2.next

	return head3


def sum_list(head1,head2,head3):
	remainder = 0
	marker1 = head1.next
	marker2 = head2.next
	marker3 = head3

	while((marker1 != None) and (marker2 != None)):
		sum  = (marker1.value + marker2.value + remainder)%10
		remainder  = (marker1.value + marker2.value + remainder)//10
		temp = Node(sum)
		marker3.next = temp
		marker3 = marker3.next

		marker1 = marker1.next
		marker2 = marker2.next

	temp = Node(remainder)
	marker3.next = temp
	head3 = head3.next
	return head3


a = Node(0)
a = create_list(a,5,[4,3,2,1,0])
#print_list(a)

b = Node(0)
b = create_list(b,5,[7,8,6,2,1])
#print_list(b)
z = Node(0)

z = sum_list2(a,b,z)
print_list(z)