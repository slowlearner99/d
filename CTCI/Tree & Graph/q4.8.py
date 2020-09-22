
class Node:

	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None


def findPath(root,path,k):

	if root is None:
		return False

	path.append(root.key)

	if root.key == k:
		return True

	if (root.left != None and findPath(root.left,path,k)) or (root.right!=None and findPath(root.right,path,k)):
		return True

	path.pop()

	return False

def findLCA_Path(root,n1,n2):

	path1 = []
	path2 = []

	if (not findPath(root,path1,n1)) or (not findPath(root,path2,n2)):
		return -1

	i = 0

	while((i<len(path1)) and (i < len(path2))):
		if (path1[i] != path2[i]):
			break

		i+=1

	return path1[i-1]

def findLCA_single_traversal(root,n1,n2):

	if root is None:
		return None

	if root.key == n1 or root.key == n2:
		return root

	left_lca = findLCA_single_traversal(root.left,n1,n2)
	right_lca = findLCA_single_traversal(root.right,n1,n2)

	if left_lca and right_lca:
		return root

	return left_lca if left_lca is not None else right_lca





root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
  
print "LCA(4, 5) = %d" %(findLCA_Path(root, 4, 5,)) 
print "LCA(4, 6) = %d" %(findLCA_Path(root, 4, 6)) 
print "LCA(3, 4) = %d" %(findLCA_Path(root,3,4)) 
print "LCA(2, 4) = %d" %(findLCA_Path(root,2, 4))

print(" ")

print ("LCA(4,5) = ", findLCA_single_traversal(root, 4, 5).key) 
print ("LCA(4,6) = ", findLCA_single_traversal(root, 4, 6).key) 
print ("LCA(3,4) = ", findLCA_single_traversal(root, 3, 4).key) 
print ("LCA(2,4) = ", findLCA_single_traversal(root, 2, 4).key) 

