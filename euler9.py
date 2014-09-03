sum = 1000
for a in range(1,sum/3):
	for b in range (a+1,sum/2):
		c = sum - a - b
		if (a*a + b*b == c*c):
			print a*b*c
