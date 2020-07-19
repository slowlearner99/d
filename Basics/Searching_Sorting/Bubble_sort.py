def bubbleSort(arr):

	for i in range(len(arr) - 1):

		for j in range(0,len(arr) - i - 1):

			if arr[j] > arr[j+1]:

				arr[j],arr[j+1] = arr[j+1],arr[j]

	print arr


arr = [10,9,8,7,6,5,4,3,2,1,0]
bubbleSort(arr)
