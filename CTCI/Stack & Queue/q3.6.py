class Stack:

	def __init__(self):
		self.s = []
		self.order = []

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

class Animal:

	def __init__(self):
		self.dogs = Stack()
		self.cats = Stack()
		self.order = []

	def pop(self,species = 'A'):
		if(species == 'D'):
			ret = self.dogs.pop()
			if(ret!=False):
				self.order.remove('D')
			return ret
		if(species == 'C'):
			ret = self.cats.pop()
			if(ret != False):
				self.order.remove('C')
			return ret
		if(species == 'A'):
			ret = self.order.pop()
			if(ret == 'C'):
				return self.cats.pop()
			else:
				return self.dogs.pop()
			

	def push(self,name,species):
		if species =='D':
			self.order.append('D')
			self.dogs.push(name)
		else:
			self.order.append('C')
			self.cats.push(name)

def print_stack(s1):
	if s1.is_empty():
		print "Stack is empty"
		return
	while(s1.is_empty()==False):
		print(s1.pop())

a = Animal()
a.push('Jeff','D')
a.push('Dave','C')
a.push('Tim','D')
a.push('Peter','D')
print(a.pop('D'))
print(a.pop('C'))
print(a.pop())