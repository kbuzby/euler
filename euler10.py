primes = 5
for x in range (5,2000000,2):
	for y in range(2,x):
		if x%y==0:
			break
	else:
		primes = primes + x
print primes
	
