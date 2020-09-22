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

def countPathsWithSum(node, targetSum, runningSum_y, pathCount):
	if (node):
		runningSum_y += node.item
		runningSum_x = runningSum_y - targetSum
		totalPath = pathCount[runningSum_x]

		if runningSum_y == targetSum:
			totalPath+=1

		pathCount[runningSum_y]+=1

		totalPath+=countPathsWithSum(node.left, targetSum, runningSum_y, pathCount)
		totalPath+=countPathsWithSum(node.right, targetSum, runningSum_y, pathCount)

		pathCount[runningSum_y] = 0
		return totalPath
	
	else:
		return 0;

root = Node(10)
root.left = Node(5)
root.right = Node(-3)
root.left.left = Node(3)
root.left.right = Node(2)
root.right.right = Node(11)
root.left.left.left = Node(3)
root.left.left.right = Node(-2)
root.left.right.right = Node(1)

import collections
pathCount = collections.defaultdict(int)

print(countPathsWithSum(root,8,0,pathCount))

