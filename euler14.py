x = 1000000
maxcount = 0
orignum = 0
maxnum = 0

for num in range(2,x+1):
	count = 0
	orignum = num
	while num != 1:	

		if num%2==0:
			num = num/2
		else:
			num = (3 * num) + 1
		count += 1
		if count>maxcount:
			maxcount = count
			maxnum = orignum
			print maxnum
