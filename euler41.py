import itertools
def isprime(n):
	for i in range(2,int(n**0.5)+1):
		if n%i==0:
			return False
	return True

def tup2int(tup):
	nums = " "
	for n in range(0,len(tup)):
		nums += str(tup[n])
	return int(nums)

max = 0
for x in range(9,1,-1):
	perms = sorted(list(itertools.permutations(range(1,x))), reverse=True)
	for perm in perms:
		num = tup2int(perm)
		if num > max and isprime(num):
			print num
			max = num
			break
	if max > 0:
		break
	
