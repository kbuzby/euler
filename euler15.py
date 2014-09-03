def factorial(n):
	factorialValue=1
	while n > 1:
		factorialValue *=n
		n -= 1
	return factorialValue

def number_combos(n, k):
	numberOfCombos = factorial(n) / (factorial(k) * factorial(n - k))
	return numberOfCombos

print (number_combos(40, 20))
