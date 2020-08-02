def isUnique(item):
	s = set(item)
	if (len(item)==len(s)):
		return True
	else:
		return False

item = 1,2,2,4
print(isUnique(item))
item = 1,2,3,4
print(isUnique(item))