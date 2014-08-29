x=5
primes = 3
prime = 0
count = 2
while count<10001:
	prime = 0
	for y in range(2,x):
		if x%y!=0:
			prime=prime+1
		else:
			prime = 0
			x=x+1
			y=2
		if prime==x-2:
			primes = x
			count = count + 1
			x = x+1
	print count
	print primes
	
