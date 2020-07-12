#Given an array of Integers find the largest contiguos sum 

def large_cont_sum(arr):
	
	if len(arr) == 0:
		return 0;

	max_sum = current_sum = arr[0]

	for num in arr[1:]:
		print 'num ',num
		current_sum = max(current_sum+num,num)
		print 'current_sum ',current_sum
		max_sum = max(current_sum,max_sum)
		print 'max_sum ',max_sum

		print '\n'
	return max_sum

print large_cont_sum([1,2,-1,3])


