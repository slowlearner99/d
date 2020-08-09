class Stack:

	def __init__(self):
		self.s = []

	def push(self,e):
		self.s.append(e)

	def pop(self):

		if len(self.s) == 0:
			return False

		else:
			return self.s.pop()

	def  top(self):

		if len(self.s)  == 0:
			return False

		else : 
			return self.s[-1]

	def is_empty(self):
		return len(self.s) == 0

	def length(self):
		return len(self.s)

def print_stack(s1):
	if s1.is_empty():
		print "Stack is empty"
		return
	while(s1.is_empty()==False):
		print(s1.pop())

def sort_stack(s1):
	s2 = Stack()
	pivot = s1.pop()
	s2.push(pivot)
	for i in range(s1.length()):
	 	pivot = s1.pop()
	 	if s2.top() < pivot:
	 		s2.push(pivot)
	 	else:
	 		counter = 0
	 		top_s2 = s2.top()
	 		while(top_s2>pivot):
	 			counter +=1
	 			temp_pivot = s2.pop()
	 			s1.push(temp_pivot)
	 			top_s2 = s2.top()
	 		s2.push(pivot)
	 		while(counter>0):
	 			temp_pivot = s1.pop()
	 			s2.push(temp_pivot)
	 			counter-=1
	print_stack(s2)

s1 = Stack()
s1.push(5)
s1.push(4)
s1.push(3)
s1.push(2)
s1.push(1)

print_stack(s1)
s1.push(5)
s1.push(4)
s1.push(3)
s1.push(2)
s1.push(1)

sort_stack(s1)


