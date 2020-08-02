##this uses hadhtables

import collections

d = collections.defaultdict(int)

a = 'malayalam'

count = 0

for i in a:
	d[i] += 1

for i in a:

	if(d[i]%2 == 1):
 		count+=1

if(count > 1):
	print(False)

else:
	print(True)