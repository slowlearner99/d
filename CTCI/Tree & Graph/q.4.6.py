class Node:
	def __init__(self,item):
		self.item = item
		self.parent = None
		self.left = None
		self.right = None

def inorderSuccessor(root,node):
	if(root):
		if(node.right):

			temp = node.right
			while(temp.right != None):
				temp = temp.right
			return temp.item

		if node.left:

			temp = root
			while(temp.item != node.item):
				if(temp.item >= node.item):
					successor = temp
					temp = temp.left
				else:
					temp = temp.right

			return successor.item

def inorder(root):
	if(root):
		inorder(root.left)
		print(root.item,' ',end='')
		inorder(root.right)

root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.right = Node(11)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right.right = Node(1)

inorder(root)
print();

print('5',':',inorderSuccessor(root,root.left))
print('3',':',inorderSuccessor(root,root.left.left))
print('-3',':',inorderSuccessor(root,root.right))