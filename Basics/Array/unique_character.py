##check if comprised of unique characters
import collections
def uni_char(s):
	d = collections.defaultdict(int)
	flag = 1;
	for c in s:
		d[c]+=1
		if d[c] > 1 :
			return 0

	if flag == 1 :
		return 1

def uni_char2(s):
	return len(set(s)) == len (s)

a = uni_char('absoluteabso')
if (a == 0):
	print 'Not Unique'

elif (a == 1):
	print 'Unique'


a = uni_char2('absolute')
if (a == 1):
	print 'Unique'

elif (a == 0):
	print 'Not Unique'
