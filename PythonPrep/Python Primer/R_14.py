def prod_odd(distval):
	for i in distval:
		for j in distval:
			if (i * j)%2 == 1 and i != j:

					print(i,j)


distval = 1,2,3,4,5,6,7,8,9,10
prod_odd(distval)