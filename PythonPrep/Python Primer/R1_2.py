def is_even(k):
	iter = True
	for i in range(k):
		if iter == False:
			iter = True
		else:
			iter = False
	return iter

print is_even(10)
print is_even(12)
print is_even(15)
