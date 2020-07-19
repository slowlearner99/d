##Binary heap is a complete binary tree 
## It can be minimum Heap or Max Hepa. The Key at the root must be minimum among all keys present in the bnary heap 


class BinHeap:

	def __init__(self):
		self.heaplist = [0] ##simple integer diviosn purpose
		self.currentSize = 0

	def heap_property(self,i):
		while i // 2 > 0:
			if self.heaplist[i] < self.heaplist[i//2]:
				tmp = self.heaplist[i//2]
				self.heaplist[i//2] = self.heaplist[i]
				self.heaplist[i] = tmp
			i = i // 2

	def insert(self,k):
		self.heaplist.append(k)
		self.currentSize = self.currentSize + 1
		self.heap_property(self.currentSize)

	def  minChild(self,i):
		if i*2 + 1 > self.currentSize:
			return i * 2
		else :
			if self.heaplist[i*2] < self.heaplist[i*2+1]:
				return i*2
			else:
				return i*2 + 1


	def heap_structure(self, i):
		while (i*2) < = self.currentSize:
			mc = self.minChild(i)
			if self.heaplist[i] > self.heaplist[mc]
				tmp = self.heaplist[i]
				self.heaplist[i] = self.heaplist[mc]
				self.heaplist[mc] = tmp
			i = mc

	def delMin(self):

		 retval = self.heaplist[1]
		 self.heaplist[1] - self.heaplist[self.currentSize]
		 self.currentSize = self.currentSize - 1
		 self.heaplist.pop()
		 self.heap_structure(1)
		 return retval

	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heaplist = [0]+ alist[:]
		while(i > 0):
			self.heap_structure(i)
			i = i - 1






