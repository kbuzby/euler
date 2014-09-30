def getprimes(n):
	numbers = set(range(n,1,-1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2,n+1,p)))
	return primes

ans = 0
total = 0
primes = getprimes(800000)
while ans<11:
	for prime in primes:
		if prime>=10:
			pstr = str(prime)
			test = 1
			for x in range(1,len(pstr)):
				if int(pstr[x:]) in primes and int(pstr[:-x]) in primes:
					test += 1
			if test == len(pstr):
				ans += 1
				total += prime
				print prime
	print 'out of bounds'
	break
print total
