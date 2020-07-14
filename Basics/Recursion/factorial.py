def fact(n):
	if n == 0: #base_case
		return 1

	else: 
		return n*fact(n-1)

print fact (5)