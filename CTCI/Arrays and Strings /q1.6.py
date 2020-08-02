
def compress(a):
	nl = []
	i = 0
	counter = 1
	pivot = a[0]
	nl.append(pivot)

	while(i < len(a)):

		if (i != len(a)-1) and (a[i+1] == pivot):
			counter+=1
		
		if (i != len(a)-1) and (a[i+1] != pivot):
			nl.append(str(counter))
			counter = 1
			pivot = a[i+1]
			nl.append(pivot)
		
		if (i == len(a)-1):
			nl.append(str(counter))
		
		i+=1

	if(len(nl)>=len(a)):
		return(a)

	else:
		return(nl)

a = 'aabcccccaaa'
print(''.join(compress(a)))