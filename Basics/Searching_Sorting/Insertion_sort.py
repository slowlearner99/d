def insertionsort(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0  and key < arr[j] : 
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	print arr


arr = [10,9,8,7,6,5,4,3,2,1,0]
insertionsort(arr)
