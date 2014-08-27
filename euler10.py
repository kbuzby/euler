def get_primes(n):
	numbers = set(range(n,1,-1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2,n+1,p)))
	return primes


primes = get_primes(2000000)
sumprime = 0

for x in range(0,len(primes)):
	sumprime = sumprime + primes[x]
print sumprime
