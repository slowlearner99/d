##on^2 time
def oneaway_bruteforce(a,b):
	i = 0

	while((i != len(a)) and (b != [])):

		if a[i] in b:
			temp = a[i]
			a.remove(temp)
			b.remove(temp)

			if i!= 0:
				i-=1

		else: 
				i+=1

	if((len(a) > 1) or (len(b) > 1)) :
		return False

	else:
		return True

##o(n) time

def oneaway(a,b):

	if (abs(len(a) - len(b)) > 1):
		return False

	if(len(a) < len(b)):
		s1 = a
		s2 = b

	else:
		s1 = b
		s2 = a

	flag = False

	index1 = 0
	index2 = 0

	while(index1 < len(s1)) and (index2 < len(s2)) : 

		if(s1[index1] != s2[index2]):
		
			if(flag):
				return False
		
			flag = True

			if(len(a)  == len(b)):
				index1+=1
		else:
			index1+=1

		index2+=1

	return True


a = list('pale')
b = list('ple')
print(oneaway(a,b))
a = list('pales')
b = list('pale')
print(oneaway(a,b))
a = list('pale')
b = list('bale')
print(oneaway(a,b))
a = list('pale')
b = list('bake')
print(oneaway(a,b))
a = list('appe')
b = list('apple')
print(oneaway(a,b))