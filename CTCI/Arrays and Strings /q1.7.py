def rotmat_brute(a):

	b = [[0]*len(a) for j in range(len(a))]
	iter1 = 0
	iter2 = len(a) - 1
	
	while(iter1 <len(a) and iter2 >= 0):
		i = 0

		while(i<len(a)):
			b[iter1][i] = a[i][iter2]
			i+=1

		iter1+=1
		iter2-=1

	return b

def rotmat(a):

	if (len(a)!=len(a[0])) and len(a) == 0:
		return "Not a Square Matrix"

	n = len(a)

	layer = 0
	while(layer < (n/2)):

		first = layer
		last = n - 1 - layer

		i = first

		while(i < last):


			offset = i - first	
			top = a[first][i]

			##left -> top
			a[first][i] = a[last-offset][first]

			## bottom ->left
			a[last-offset][first] = a[last][last-offset]

			##right -> bottom
			a[last][last-offset] = a[i][last]

			##top->right 
			a[i][last] = top ##right saved to top

			i+=1


		layer += 1

	return a



a = [[0,3,6],[1,4,7],[2,5,8]]
print(a[0])
print(a[1])
print(a[2])
a = rotmat_brute(a)
print()
print(a[0])
print(a[1])
print(a[2])

print()

a = [[0,3,6],[1,4,7],[2,5,8]]
print(a[0])
print(a[1])
print(a[2])
a = rotmat(a)
print()
print(a[0])
print(a[1])
print(a[2])