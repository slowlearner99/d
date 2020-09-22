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

def countPathswithSum(root,targetSum):
	if(root):
		paths_from_root = countPathFromNode(root,targetSum,0)
		paths_from_lc = countPathswithSum(root.left,targetSum)
		paths_from_rc = countPathswithSum(root.right,targetSum)
		return paths_from_root + paths_from_lc + paths_from_rc
	else:
		return 0

def countPathFromNode(root,targetSum,currentSum):
	if(root):
		currentSum += root.item;
		totalPath = 0

		if  currentSum == targetSum:
			totalPath+=1

		totalPath+=countPathFromNode(root.left,targetSum,currentSum)
		totalPath+=countPathFromNode(root.right,targetSum,currentSum)

		return totalPath

	else:
		return 0



root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.right = Node(11)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right.right = Node(1)

print(countPathswithSum(root,8))
