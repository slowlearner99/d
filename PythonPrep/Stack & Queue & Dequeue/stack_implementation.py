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


a = Stack()
print a.is_empty()
a.push(1)
a.push(2)
a.push(3)
print a.length()
print a.top()
a.pop()
print a.length()
print a.top()
a.pop()
print a.length()
print a.top()
a.pop()
print a.length()
print a.top()