def solutions(p):
	sols = []
	for a in range(1,p-1):
		for b in range(1,p-a):
			c = p - a - b
			if ((a**2)+(b**2))==(c**2) and (a+b+c)==p:
				if sorted([a,b,c]) not in sols:
					sols.append([a,b,c])
	return len(sols)

max = 0
ans = 0
for p in range(3,1001):
	temp = solutions(p)
	if temp>max:
		max = temp
		ans = p
print ans
				
