def selectionsort(arr):

	for i in range(len(arr)):

		min_index = i
		for j in range(i+1,len(arr)):
			if arr[min_index] > arr[j]:
				min_index = j  

		arr[i],arr[min_index] = arr[min_index],arr[i]
		print arr

arr = [10,9,8,7,6,5,4,3,2,1,0]
selectionsort(arr)