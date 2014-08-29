divisors = 0
i = 1
num = 0

def factors(n):
	return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

while divisors<500:
	num = sum(range(1,i+1))
	divisors = 0
	factorlist = factors(num)
	divisors = len(factorlist)
	i+=1
print num
