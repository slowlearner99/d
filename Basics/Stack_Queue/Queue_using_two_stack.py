class Queue2Stacks:

	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def enqueue(self,item):
		self.stack1.append(item)

	def dequeue(self):
		for i in range(len(self.stack1)):
			self.stack2.append(self.stack1.pop())
		print self.stack2.pop()
		self.stack1 = self.stack2
		self.stack2 = []

	def size(self):
		return len(self.stack1)

	def isEmpty(self):
		return self.stack1 == []

q = Queue2Stacks()
print q.size()
print q.isEmpty()
q.enqueue(1)
q.enqueue(2)
print q.dequeue()