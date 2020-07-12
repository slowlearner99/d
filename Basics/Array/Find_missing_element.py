# Array of non -ve int,
# 2 nd array by shuffling input and deleting random element
# Find missing element in the second array 

def finder(arr1,arr2):
	arr1.sort();
	arr2.sort();

	if arr1 == arr2:
		print 'No Deleted Element'

	for i in arr1:
		if i not in arr2:
			return i

print finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])


## Solution using a Hash Table

import collections
def finder2(arr1, arr2):

	# collections are used because this will add the key to dictionay if it doesnt exist and wont throw an error

	d = collections.defaultdict(int)


	for num in arr2:
		d[num] += 1

	for num in arr1:
		if d[num] == 0 :
			return num

		else:
			d[num] -= 1

print finder2([5,5,7,7],[5,7,7])


# another approach is to subtract sums if arrays are too large and numbers are too small

#Best solutions is to XOR every element in it 

def finder3(arr1,arr2):
	result=0

	#Perform XOR between the arrays

	for num in arr1+arr2:
		result ^= num
		print result

	return result

print finder3([5,5,7,7],[5,7,7])
