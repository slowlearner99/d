import random

class Node:
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None
		self.size = 1

	def get_size(self):
		return self.size

	def get_item(self):
		return self.item

	def getRandomNode(self):
		if(self.left):
			leftSize = self.left.get_size();
		else:
			leftSize = 0

		index = random.randint(0,self.get_size())

		if(index < leftSize):
			if(self.left):
				return self.left.getRandomNode()
			else:
				return self.item

		elif (index == leftSize):
			return self.item

		else:
			if (self.right):
				return self.right.getRandomNode()
			else:
				return self.item

	def insertInOrder(self,item):
		if(item<self.item):
			if(self.left):
				self.left.insertInOrder(item)
			else:
				self.left = Node(item)
		else:
			if(self.right):
				self.right.insertInOrder(item)
			else:
				self.right = Node(item)
		self.size+=1

	def find(self,value):
		if self.item == value:
			return self
		elif (value <= self.item):
			if(self.left):
				self.left.find(value)
			else:
				return None
		elif(value >= self.item):
			if(self.right):
				self.right.find(value)
			else:
				return None

		else:
			return None


root = Node(10)
root.insertInOrder(5)
root.insertInOrder(-3)
root.insertInOrder(3)
root.insertInOrder(2)
root.insertInOrder(11)
root.insertInOrder(3)
root.insertInOrder(-2)
root.insertInOrder(1)

print(root.getRandomNode())
