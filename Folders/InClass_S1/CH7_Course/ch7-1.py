def factorial(x):
	if x == 1:
		return 1
	return x * factorial(x-1)

print(factorial(5))
'''
5*factorial(x-1)
4*factorial(x-1)
3*factorial(x-1)
2*factorial(x-1)
'''