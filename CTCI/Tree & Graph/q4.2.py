### binary search tree with minimum height

class Node:
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None

def create_tree(tree,start,stop):
	if stop > start:

		mid = (start + start)//2
		root = Node(tree[mid])
		root.left = create_tree(tree,start,mid-1)
		root.right = create_tree(tree,mid+1,stop)
		return root

	else:

		return None

def inorder(root):

	if(root):
		inorder(root.left)
		print(root.item)
		inorder(root.right)


tree = [1,2,3,4,5,6,7]
root = Node(0)
root = create_tree(tree,0,len(tree))
inorder(root)