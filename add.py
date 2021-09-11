def add_two_numbers(a, b):
	return a+b

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = add_two_numbers(a,b)
print('The sum of {0} and {1} is {2}'.format(a, b, c))
