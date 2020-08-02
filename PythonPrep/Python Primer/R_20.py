import random
def shuffle(data):
	ret = []
	while(data):
		index = random.randint(0,len(data)-1)
		ret.append(data[index])
		data.pop(index)
	return ret

data = [1,2,3,4,5]
print(shuffle(data))
