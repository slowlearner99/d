def rotation(str1,str2):
	#str1 is the rotated string 
	#str2 is the parent string 
	return substring(str2, str1+str1)

def substring(s1,s2):
	return s1 in s2

a = 'waterbottle'
b = 'terbottlewa'

print(rotation(a,b))