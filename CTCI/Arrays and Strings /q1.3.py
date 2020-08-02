
##Brute Force Approach n2 time 
a = list('Mr John Smith')

for k in range(len(a)):

 	if a[k] == ' ':
 		b = len(a)
 		b = b - 1
 		a.append(1)
 		a.append(2)

 		while( b > k ):
			
 			a[b+2] = a[b]
 			b-=1

 		a[k] = "%"
 		a[k+1] = "2"
 		a[k+2] = "0"


print(''.join(a))

## Optimised Approach n time 

a = list('Mr John Smith')
n = 0	
b = len(a)-1

for k in a:
	if k == ' ':
		n+=1

for i in range(2*n): ##making spcae in front
	a.append('1')

k = len(a)-1

while (k >= 0 ):

  	if a[b] == ' ':
 
  		a[k] = '0'
  		a[k-1] = '2'
  		a[k-2] = '%'

  		k = k - 3
  		b = b - 1
  

  	else :

  		a[k] = a[b]
  		b = b - 1
  		k = k - 1

print(''.join(a))