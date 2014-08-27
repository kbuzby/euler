def get_primes(n):
	numbers = set(range(n,1,-1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2,n+1,p)))
	return primes

num = 600851475143

primes = get_primes(100000)
highprime = 0

for x in range(0,len(primes)):
	if (num%primes[x]==0):
		num = num/primes[x]
		highprime=primes[x]
		print highprime
