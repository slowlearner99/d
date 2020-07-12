## given an integer array, output unique pairs that sum up to a specific value K. 

## iterative method 
## sort_and_find

def pair_sum(arr,k):

	#Edge case
	if len(arr) < 2:
		return

	#Sets for Tracking
	seen = set()
	output = set()

	#For every number in array 
	for num in arr:

		target = k - num;

		if target not in seen: 
			seen.add(num)

		else: 
			output.add(((min(num,target)), max(num,target)))

print '\n'.join(map(str,list(output)))


pair_sum([1,3,2,2],4)