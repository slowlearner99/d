def binarySearch(arr,index):

	if len(arr) <= 1 and arr[0] != index:
		print 'Not Found'
		return False

	else:
		mid = len(arr)/2

		if(arr[mid] == index):
			print 'Found'
			return True	
		else:		
			if(index < arr[mid]):
				
				binarySearch(arr[:mid],index)
					
			else:

				binarySearch(arr[mid:],index)


arr = [1,2,3,4,5,6,7,8,9,10]
binarySearch(arr,1)
binarySearch(arr,2)
binarySearch(arr,3)
