import math
def getprimes(n):
	numbers = set(range(n,1,-1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2,n+1,p)))
	return primes

max = 0
prod = 0
primes = getprimes(100000)
b1 = getprimes(1000)
b2 = [x*(-1) for x in b1]
bs = sorted(b1 + b2)
for a in range(-1000,1000):
	for b in bs:
		n = 0
		temp = 0
		quad = (n**2) + (a*n) + b
		while quad in primes:
			temp += 1
			n += 1
			quad = (n**2) + (a*n) + b
		if temp>max:
			max = temp
			prod = a*b
			print max
			print str(a) + " * " + str(b) + " = " + str(a*b)	
