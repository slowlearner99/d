# string of opening and closeing paranthesis check if it is balanced
# 3types of paranthesis [] {} () 
# String contains no other character


def balance_check(s):
	stack = []
	flag = 1
	for i in s:
		if i in ('{','(','[') :
			stack.append(i)
		else:
			if i == '}':

				if stack[len(stack)-1] == '{':
					stack.pop() 

				else:
					flag = 0
					break;

			elif i == ')':

				if stack[len(stack)-1] == '(':
					stack.pop() 

				else:
					flag = 0
					break;

			
			elif i == ']':

				if stack[len(stack)-1] == '[':
					stack.pop() 

				else:
					flag = 0
					break;

	if flag == 0:
		return False
	else: 
		return True

	if stack == []:
		return True
	else:
		return False

print balance_check('((({})))')