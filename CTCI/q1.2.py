def checkperm(s1,s2):
	s1.sort() ##nlogntime
	s2.sort()
	return s1 == s2


s1 = list('dodge')
s2 = list('dogde')

print checkperm(s1,s2)

##using hash tables n time

import collections

def checkperm2(s1,s2):

	d = collections.defaultdict(int)
	for i in s1:
		d[i]+=1
	for i in s2:

		if(d[i] > 0):
			d[i]-=1
		else:
			return False

	if (not d):		
		return False
	else:
		return True

print checkperm2(s1,s2)

## using constant time solution

def checkperm3(s1,s2):

	result=0

	if len(s1) !=len(s2):
		return False

	#Perform XOR between the arrays

	for num in s1+s2:
		result ^= num 

	if result:
		return False
	else:
		return True

print checkperm3([1,2,3,4,5],[5,4,3,2,1])