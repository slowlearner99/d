tree_vals = []

def inorder(tree):
	if tree != None:
		inorder(tree.getLeftChild())
		tree_vals.append(tree.getRootVal())
		inorder(tree.getRightChild())

def sort_check(tree_val):
	return	tree_vals == sorted(tree_vals)

inorder(tree)
sort_check(tree_vals)