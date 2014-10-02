max = 0

for a in range(99,1,-1):
	for b in range(99,1,-1):
		numstr = str(a**b)
		val = 0
		for c in numstr:
			val += int(c)
			if val > max:
				max = val
				print max

