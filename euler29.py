upper = 100
ans = []
for a in range(2,upper+1):
	for b in range(2,upper+1):
		num = a**b
		if len(ans) != 0:
			unique = False
			for check in ans:
				if num == check:
					unique = False
					break
				else:
					unique = True
			if unique:
				ans.append(a**b)
		else:
			ans.append(a**b)
		
print len(ans)
