def set_row_zero(i,matrix):
	for j in range(len(matrix)):
		matrix[i][j] = 0

	return matrix

def set_column_zero(i,matrix):
	for j in range(len(matrix[0])):
		matrix[j][i] = 0

	return matrix

def zeromat(matrix): ##(OMN) Space Complexity

	row_zero = set()
	column_zero = set()
	i = 0

	while(i < len(matrix)):
		j = 0
		while(j < len(matrix[0])):
			if matrix[i][j] == 0:
				row_zero.add(i)
				column_zero.add(j)
				break
			j+=1
		i+=1

	for i in row_zero:
		a = set_row_zero(i,matrix)

	for i in column_zero:
		a = set_column_zero(i,matrix)

	return a

def zeromat_const(matrix): ##constant time

	i = 0
	while(i<len(matrix)):
		j = 0		
		while(j<len(matrix)):
			if matrix[i][j] == 0:
				matrix[i][0] = 0	
				matrix[0][j] = 0

			j+=1
		i+=1

	for i in range(len(matrix)):
		if matrix[i][0] == 0:
			matrix = set_row_zero(i, matrix)

	for j in range(len(matrix[0])):
		if matrix[0][j] == 0:
			matrix = set_column_zero(j, matrix)

	return matrix

a = [[1,3,6],[1,0,7],[2,5,8]]

a = zeromat(a)
print(a)

a = [[1,3,6],[1,0,7],[2,5,8]]

a = zeromat_const(a)
print(a)