
def fib(value):

	if value == 0:
		return 0

	if value == 1:
		return 1

	return fib(value-1) + fib(value-2)

print fib(5)
print fib(10)