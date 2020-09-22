class BinaryTree(object):

	def __init__(self,rootobj):
		self.key = rootobj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self,newNode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(newNode)

		else:
			t = BinaryTree(newNode)
			t.leftChild = self.self.leftChild
			self.leftChild = t

	def insertRight(self,newNode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newNode)

		else:	
			t = BinaryTree(newNode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self,obj):
		self.key = obj

	def getRootVal(self):
		return self.key

def inorder(root):
	if(root):
		print(root.getRootVal())
		inorder(root.getLeftChild())
		inorder(root.getRightChild())

def postorder(root):
	if(root):
		postorder(root.getLeftChild())
		postorder(root.getRightChild())
		print(root.getRootVal())

def preorder(root):
	if(root):
		print(root.getRootVal())
		preorder(root.getLeftChild())
		preorder(root.getRightChild())

root  = BinaryTree(1)
root.insertRight(3)
root.insertLeft(2)
rt = root.getRightChild()
lt = root.getLeftChild()
lt.insertLeft(4)
lt.insertRight(5)
rt.insertLeft(6)
rt.insertRight(7)
print('preorder')
preorder(root)
print('postorder')
postorder(root)
print('inorder')
inorder(root)















