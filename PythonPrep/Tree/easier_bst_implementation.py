class Node:
 	def __init__(self,key):
 		self.key = key
 		self.leftChild = None
 		self.rightChild = None

def inorder(root): 
    if root is not None: 
        inorder(root.leftChild) 
        print root.key, 
        inorder(root.rightChild) 

def insert(node, key): 

     if node is None: 
         return Node(key) 
  
     if key < node.key: 
         node.leftChild = insert(node.leftChild , key) 
     else: 
         node.rightChild = insert(node.rightChild, key)  
    
     return node

def minValueNode(node):
	current = node
	while(current.leftChild is not None ):
		current = current.leftChild

	return current

def delNode(root, key): 

    if root is None: 
        return root  
  
    if key < root.key: 
        root.leftChild = delNode(root.leftChild , key) 
  

    elif(key > root.key): 
        root.rightChild = delNode(root.rightChild , key) 
  

    else: 
          
 
        if root.leftChild is None : 
            temp = root.rightChild  
            root = None 
            return temp  
              
        elif root.rightChild is None : 
            temp = root.leftChild 
            root = None
            return temp 
 
        temp = minValueNode(root.rightChild) 
        root.key = temp.key 

        root.rightChild = delNode(root.rightChild , temp.key) 
  
  
    return root
  

root = None
root = insert(root, 50) 
root = insert(root, 30) 
root = insert(root, 20) 
root = insert(root, 40) 
root = insert(root, 70) 
root = insert(root, 60) 
root = insert(root, 80) 
  
print "Inorder traversal of the given tree"
inorder(root) 
  
print "\nDelete 20"
root = delNode(root, 20) 
print "Inorder traversal of the modified tree"
inorder(root) 
  
print "\nDelete 30"
root = delNode(root, 30) 
print "Inorder traversal of the modified tree"
inorder(root) 
  
print "\nDelete 50"
root = delNode(root, 50) 
print "Inorder traversal of the modified tree"
inorder(root)






