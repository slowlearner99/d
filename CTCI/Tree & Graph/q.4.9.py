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

def list_of_depths(node,level,depths):
	if (node):
		depths[level].append(node.item)
		list_of_depths(node.left,level+1,depths)
		list_of_depths(node.right,level+1,depths)


from collections import defaultdict
depths = defaultdict(list)
perm = defaultdict(list)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

list_of_depths(root,0,depths)

import itertools

for i in range(3):
	permutations_object = itertools.permutations(depths[i])
	permutations_list = list(permutations_object)
	perm[i] = permutations_list


for i in perm[0]:
	for j in perm[1]:
		for k in perm[2]:
			print(i,j,k)


			