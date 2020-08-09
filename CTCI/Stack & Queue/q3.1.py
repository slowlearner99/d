array = [0 for i in range(100)] ##initialise an array 
n = 100/3

max_size = []
max_size.append(-1)
max_size.append(n//1)
max_size.append(2*n//1)
max_size.append(3*n)


top = []
top.append(-1)
top.append(max_size[0])
top.append(max_size[1])
top.append(max_size[2])


def push(stack, element):
 	if top[stack] == max_size[stack]:
 	  	return "Stack Overflow"
 	else:
 	  	top[stack] += 1
 	  	array.insert(top[stack],element)
 	  	return "Element Inserted"


def pop(stack):
 	if top[stack] == max_size[stack-1]:
  		return	"Stack Underflow"
  	else:
  		top[stack] -=1
  		return array[top[stack] + 1]


def stack_top(stack):
   	if top[stack] == max_size[stack-1]:
   	 	return "Empty Stack"
   	else:
   	 	return array.index(top[stack])

def is_empty(stack):
  	return top[stack] == max_size[stack-1]


print(push(1,1))
print(stack_top((1)))
print(stack_top((2)))
print(push(2,1))
print(push(2,2))
print(is_empty(2))
print(pop((2)))