
class BinaryTree(object):

	def __init__(self,rootObj):

		self.key  = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
		
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)

		else: 
			##Push existing left child down one level
			t = BinaryTree(newNode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self,newNode):
		
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)

		else:

			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		if self.rightChild == None:
			return 'No Right Child'
		return self.rightChild.key

	def getLeftChild(self):
		if self.leftChild == None:
			return 'No Left Child'
		return self.leftChild.key

	def setRootVal(self,obj):
		return self.key == obj


	def getRootval(self):
		return self.key


r = BinaryTree('a')
print r.getRootval()
print r.getRightChild()
r.insertRight('b')
print r.getRightChild()
print r.getLeftChild()
r.insertLeft('c')
print r.getLeftChild()