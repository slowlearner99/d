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

class Queue:

	def __init__(self):
		self.a = Stack()
		self.b = Stack()

	def enqueue(self,item):
		self.a.push(item)

	def dequeue(self):
		while(self.a.is_empty()!=True):
			temp = self.a.pop()
			self.b.push(temp)
		tmp = self.b.pop()
		while(self.b.is_empty() != True):
			temp = self.b.pop()
			self.a.push(temp)
		return tmp


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())









