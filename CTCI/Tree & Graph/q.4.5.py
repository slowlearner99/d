class Node:
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None

def inorder(root):
	if(root):
		inorder(root.left)
		print(root.item)
		inorder(root.right)

def node_satisfy_bst(node):
	if(node):
		leftChild = node.left
		rightChild = node.right
		if leftChild:
			if leftChild.item > node.item:
				return False
		if rightChild:
			if rightChild.item < node.item:
				return False
		return True

def check_bst(node):
	if node:
		if node_satisfy_bst(node) == False:
			return False
		else:	
			a = check_bst(node.right)
			b = check_bst(node.left)
			if (a == False) or (b== False):
				return False 
			else:
				return True

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)


print(check_bst(root))

root = Node(4)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.left = Node(5)
root.right.right = Node(7)

print(check_bst(root))