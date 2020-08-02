def minmax(data):
	min = data[0]
	max = data[0]
	for i in data:
		if i < min:
			min = i
		if i > max:
			max = i
	return min,max

print minmax([1,2,3,4,5,6,7,8])
print minmax([9,8,7,6,5,4,3,2])