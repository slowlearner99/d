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

def check_balance(node):
	if(node):
		rightt = check_balance(node.right)
		if rightt == None:
			return False
		leftt = check_balance(node.left)
		if leftt == None:
			return False

		height_diff = check_balance(node.left) - check_balance(node.right)
		if(abs(height_diff)>1):
			return False
	else:
		return 1


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

flag = check_balance(root)
if(flag):
	print('The Tree is balanced')
else:
	print('The Tree is not balanced') 