class Stack:

	def __init__(self):
		self.s = []
		self.min = []

	def push(self,e):
		if(self.min	== []):
			self.min.append(e)

		if(self.min[-1] > e):
				self.min.append(e)
		self.s.append(e)

	def pop(self):
		if len(self.s) == 0:
			return False
		else:
			if(self.min[-1] == self.s[-1]):
				self.min.pop()

			return self.s.pop()

	def top(self):

		if len(self.s)  == 0:
			return False

		else : 
			return self.s[-1]

	def is_empty(self):
		return len(self.s) == 0

	def length(self):
		return len(self.s)

	def minimum(self):
		if len(self.min)  == 0:
			return False

		else : 
			return self.min[-1]

s = Stack()
s.push(5)
s.push(4)
s.push(10)
s.push(3)
print(s.minimum())
s.pop()
print(s.minimum())
s.pop()
print(s.minimum())
s.top()