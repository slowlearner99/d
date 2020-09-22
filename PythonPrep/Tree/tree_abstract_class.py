class Tree:

	##Abstract class representing a tree structure

	class Position:

		###An abstraction represting the location of single element 

		def elements(self):
			### Return the element stored at this position 

			raise NotImplementedError('Must be implemented by a subclass')

		def __eq__(self, other):
			###Return true if position represents the same location 
			raise NotImplementedError('Must be implemented by subclass')

		def __ne__(self,other):
			###Return true if they do not represent the same location 
			return not (self == other)


	##Abstract methods a concrete subclass must support
	def root(self):
		###Return postiion representing the trees root
		raise NotImplementedError('Must be implemented a subclass')

	def parent(self,p)
		### Return position representing ps parent 
		raise NotImplementedError('Must be implemented a subclass')	

	def num_children(self,p):
		### Return he number of children that Position p has 
		raise NotImplementedError('Must be implemented a subclass')	

	def children(self,p):
		###Generate iteration of postitions representing sp children
		raise NotImplementedError('Must be implemented a subclass')	

	def __len__(self):
		###Return total number of elements in a tree
		raise NotImplementedError('Must be implemented a subclass')	

	###concrete methods implemented in this class

	def is_root(self,p):
		##return true if the postition represents the root of the tree
		return self.root() == p

	def is_leaf(self,p):
		###return true if position p does not have any children
		return self.num_children(p) == 0

	def is_empty(self):
		##return true if the tree is empty
		return len(self) == 0


class BinaryTree(Tree):
	###Abstract class representing a binary tree structure
	### ADditional abstract methods
	def left(self, p):
	###REturn a position representing ps left child else None 
		raise NotImplementedError('Must be implemented a subclass')

	def right(self,p):
	###Return a position representing ps right child else None 
		raise NotImplementedError('Must be implemented a subclass')

	###Concrete methods implemented in this class

	def sibling(self,p):
		###Return a postiion representing ps sibling(or None if no sibling)
		parent = self.parent(p)
		if parent is None:
			return None 
		else 
			if p == self.left(parent):
				return self.right(parent)
			else:
				return self.left(parent)

	def children(self,p):
		##Genereate a iterationi of position representing ps children
		if self.left(p) is not None:
			yield self.left(p)

		if self.right(p) in not None:
			yield self.right(p)

class LinkedBinaryTree(BinaryTree):

	##Linked Representation of the Binary Node STructure 

	class _Node:
		__slots__ = '_element','_parent', '_left','_right'
		def __init__(self, element, parent = None, left = None, right = None):
			self._element = element
			self._parent = parent
			self._left = left
			self._right = right

	class Position(BinaryTree.Position):
		## Abstraction representing the lcoation of a single element 
		def __init__(self,container,node):
			##constructor
			self.container = container
			self._node = node

		def element(self):
			return self._node._element

		def __eq__(self,other):
			##True if position represents the same location
			return type(other) is type(self) and other._node is self._node

		def validate(self,p):
			##Return associated node if position is valid
			if not isinstance(p,self.postiion)
				raise TypeError('P must be proper position Type')

			if p._container is not self:
				raise ValueError('p does not belong to this container')

			if p._node._parent is p._node:
				raise ValueError('p is no longer valid')

			return p._node

		def _make_position(self,node):
			##Return position instance for given node or Node if no node
			return self.Position(self,node) if node is not None else None 


		##binary tree constructor
		def __init__(self):
			self._root = None
			self._size = 0

		###public accessors

		def __len__(self):
			##Return the total number of elements in the tree
			return self._size

		def root(self):
			## Return the root Position of the tree of none if tree is empty 
			return self._make_position(self._root)

		def parent(self,p):
			##Return the position of ps parent (or None if p is root)

			node = self._validate(p)
			return self._make position(node._parent)

		def left(self,p):
			##return the position of ps left child
			node = self._validate(p)
			return self._make_position(node._right)

		def num_children(self,p):
			##return the number of children of position p
			node  = self._validate(p)
			node = 0
			if node._left is not None:
				count+=1
			if node._right is not None:
				count +=1
			return count 

		def _add_root(self,e):
			##pace element e at the root of an empty tree an dreturn the nre position 
			if self._root is not None :
				raise ValueError('Root Exists')
			self._size = 1
			self._root = self._Node(e)
			return self._make_position(self._root)

		def _add_left(self,p,e):
			##create a new left hild for postition p. storing element e
			## raise value error otherwise
			node = self._validate(p)
			if node._left is not None:
				raise ValueError('Left Child exist')
			self._size +=1
			node._left = self._Node(e,node)
			return self._make_position(node._left)

		def _add_right(self,p,e):
			##create a new right child for postition p, sotring element e 
			node = self._validate(p)
			if node._right is not None:
				raise ValueError('Right Child Exists')
			self._size+=1
			node._right = self._Node(e,node)
			return self._make_position(node._right)

		def _replace(self,p,e):
			##replace element at position p with e and return the old element 
			node = self._validate(p)
			old = node._element
			node._element = element
			return old

		def _delete(self,p):
			### Delete the node at position p and replace eit with its child if any 
			node = self._validate(p)
			if self.num_children(p) == 2:
				raise ValueError('p has two children')

			child = node._left if node._left else node._right

			if child is not None:
				child._parent = node._parent

			if node is self._root:
				self._root = child
			else:
				parent = node._parent
				if node is parent._left:
					parent._left = child
				else:
					parent._right = child

			self._size -=1
			node._parent = node
			return node._element

		def _attach(self,p,t1,t2):
			##attach trees t1 and t2 as left and right subtrees of external p 

			node = self._validate(p)
			if not self.is_leaf(p):
				raise ValueError('position must be leaf')
			if not type(self) is type(t1) is type(t2):
				raise TypeError('Tree Types must match')
			self._size+=len(t1) + len(t2)
			if not t1.is_empty():
				t1._root._parent = node
				node._left = t1._root
				t1._root = None
				t1._size = 0
			if not t2.is_empty():
				t2._root._parent = node
				node._right = t2._root
				t2._root = None
				t2._size = 0









































