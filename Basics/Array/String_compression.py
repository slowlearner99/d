# compress aaaabbbbccccceedddd a4b4c5e2d4

def compress(s):
	compress = []
	curele = s[0]
	counter = 0
	for i in range(len(s)):
		if(s[i] == curele):
			counter +=1

		elif(s[i] != curele):
			compress.append(curele)
			compress.append(str(counter))
			curele = s[i]
			counter = 1

	compress.append(curele)
	compress.append(str(counter))


	print ''.join(compress)

def compress2(s):
	r = ""
	l = len(s)
	if l ==0:
		return ""
	if l==1:
		return s+"1"
	last = s[0]
	cnt = 1
	i = 1

	while i < l:
		if s[i] == s[i-1]:
			cnt+=1
		else:
			r = r+s[i-1] + str(cnt)
			cnt = 1
		i += 1
	r = r + s[i-1] + str(cnt)
	return r

compress('aaaabbbbccccceedddd')
print compress2('aaaabbbbccccceedddd')


