##find if a tree is a sub tree

class Node:
	def __init__(self,item):
		self.item = item
		self.left = None
		self.right = None


def sub_tree(root1,root2):
	if(root1):
		if root1.item == root2.item:
			flag = tree_equal(root1,root2)
			if flag == True:
				return flag
		else:
			return sub_tree(root1.left,root2) or sub_tree(root1.right,root2)
	else:
		return False


def tree_equal(root1,root2): 
      
    current1 = root1  
    stack1 = [] # initialize stack 
    done1 = 0 
      
    current2 = root2
    stack2 = []
    done2 = 0

    flag = True

    while True: 
          
        if (current1 is not None) and (current2 is not None): 
              
            stack1.append(current1)
            stack2.append(current2)

            current1 = current1.left
            current2 = current2.left

        elif(stack1 and stack2):

            current1 = stack1.pop() 
            current2 = stack2.pop()

            if (current1.item == current2.item):
            	pass
            else:
            	flag = False
            	break;

            current1 = current1.right
            current2 = current2.right  
  
        else: 
            break
    return flag


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

root2 = Node(2)
root2.left=Node(1)
root2.right=Node(3)

if(sub_tree(root,root2)):
	print('T1 is a subtree of T2')
else:
	print('T1 is not a subtree of T2')

root2 = Node(2)
root2.left=Node(1)
root2.right=Node(7)

if(sub_tree(root,root2)):
	print('T1 is a subtree of T2')
else:
	print('T1 is not a subtree of T2')	
