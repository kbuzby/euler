def getprimes(n):
	numbers = set(range(n,1,-1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2,n+1,p)))
	return sorted(primes)

def isprime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

primenums = sorted(getprimes(1000000), reverse=False)

max = 20
p = 0
for i in range(0,len(primenums)-max):
	for j in range(i+max,len(primenums)):
		temp = primenums[i:j]
		if sum(temp) < 1000000 and isprime(sum(temp)) and len(temp) > max:
			max = len(temp)
			p = sum(temp)
			print max
			print p
		elif sum(temp) > 1000000:
			break
						
