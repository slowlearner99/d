def binary_search_recursive(beg,end,listt,item):

	if end > beg:

		mid = (beg + end)//2

		if listt[mid] == item:
			return mid

		elif listt[mid] > item:
			return binary_search_recursive(beg,mid-1,listt,item)

		else:
			return binary_search_recursive(mid+1,end,listt, item)

	else:
		return "Element not in the list"

def binary_search_iterative(beg,end,listt,item):
	
	while end > beg:
		mid = (beg + end)//2

		if listt[mid] == item:
			return mid

		elif listt[mid] > item:
			end = mid - 1

		else:

			beg = mid + 1

	return "Element not in the list "
	
bslist = [1,2,3,4,5,6,7,8,9,10]
length = len(bslist)
print(binary_search_recursive(0,length,bslist,7))
print(binary_search_recursive(0,length,bslist,12))

print(binary_search_iterative(0,length,bslist,7))
print(binary_search_iterative(0,length,bslist,12))