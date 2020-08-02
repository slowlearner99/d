import ctypes

class DynamicArray():

	def __init__(self):

		self._n = 0 #count actual elements
		self._capacity = 1 #default array capacity 
		self._A = self._make_array(self._capacity) #low-level array 

	def __len__(self):
		return self._n

	def __getitem__(self,k):

		if not 0 <= k <self._n :
			raise IndexError('Invalid Index')

		return self._A[k]

	def append(self, obj):

		if self._n == self._capacity:
			self._resize(2*self._capacity)

		self._A[self._n] = obj
		self._n += 1

	def _resize(self,c):

		B = self._make_array(c)
		
		for k in range(self._n):
			B[k] = self._A[k]

		self._A = B
		self._capacity = c

	def _make_array(self,c):

		return (c*ctypes.py_object)()

	def pop(self):
		if self._n == 0:
			raise IndexError('Out of Bounds')

		if self._n <= (self._capacity/4):
			self._resize((self._capacity/4))
		
		self._n = self._n - 1

arr = DynamicArray()
arr.append(1)
print(arr[0])
arr.append(2)
print(arr[0],arr[1])
arr.pop()
arr.append(3)
arr.append(4)
print(arr[0],arr[1],arr[2])