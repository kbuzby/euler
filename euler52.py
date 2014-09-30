def str2list(str):
	numlist = []
	for i in range(0,len(str)):
		numlist.append(str[i])
	return sorted(numlist)

intx = 1
while True:
	x = []
	for y in range(1,7):
		x.append(str(y * intx))
	if len(x[0]) == len(x[5]):
		base = str2list(x[0])
		count = 1
		for j in range(1,len(base)):
			if str2list(x[j]) == base:
				count += 1
		if count == 6:
			print x
			break
	intx += 1
