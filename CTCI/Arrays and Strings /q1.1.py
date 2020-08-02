def isunique1(s1):

	set1 = set()

	for i in s1:
		set1.add(i)

	if(len(s1) == len(set1)):
		return True

	else:
		return False

print isunique1('Helo')

def isunique2(s1):

	result = 0

	for num in s1:

		result ^= num ##evenoccurence1allel0

	if result:
		return True
	else:
		return False

print isunique2([1,2,3,4,5])



def inunique3(s1):

	for i in range(len(s1)):

		for j in range(i,len(s1)):

			if(i == j):

				return False

	return True

print isunique1('Helo')
# ##can use additional DS
# 1. Travesal(n2)
# 2. set datastructure
