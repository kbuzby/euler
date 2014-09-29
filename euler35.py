def getprimes(n):
	numbers = set(range(n,1,-1))
	primes = []
	while numbers:
		p = numbers.pop()
		primes.append(p)
		numbers.difference_update(set(range(p*2, n+1, p)))
	return primes

def isprime(n):
	for x in primes:
		if n%x==0:
			return False
	return True

def rotate(n):
	nstr = str(n)
	nstr = nstr[len(nstr)-1] + nstr[0:len(nstr)-1]
	return int(nstr)


ans = 0
primes = getprimes(1000000)
for num in primes:
	possible = len(str(num))
	count = 1
	test = num
#	print num
	if possible > 1:
		for x in range(0,possible-1):
			next = rotate(test)
#			print next
			if not next in primes:
				break
			else:
				count += 1
				test = next
	if count == possible:
		ans += 1
		print num
print ans
