import itertools

abundants = []

def abundant(n):
	sum = 0
	for y in range(2,n+1):
		if (n%y)==0:
			sum += (n/y)
			if sum>n:
				return True
	return False

for x in range(1,28124):
	if abundant(x):
		abundants.append(x)

nonsums = range(28124)

for m in range(0,len(abundants)):
	for n in range(0,len(abundants)):
		num = abundants[m]+abundants[n]
		if num<28124 and num in nonsums:
			nonsums.remove(num)

ans = sum(nonsums)
print ans

