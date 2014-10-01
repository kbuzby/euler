import itertools

def tup2int(tup):
	nums = " "
	for n in range(0,len(tup)):
		nums += tup[n]
	return int(nums)

perms = list(itertools.permutations('123456789'))
sols = []
for perm in perms:
	for a in range(1,4):
		t1 = tup2int(perm[0:a])
		t2 = tup2int(perm[a:5])
		t3 = tup2int(perm[5:])
		#print str(t1) + " " + str(t2) + " " + str(t3)
		if (t1 * t2) == t3:
			print t3
			sols.append(t3)

print sum(set(sols))
