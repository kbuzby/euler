max = 6*(9**5)
ans = 0
for x in range (2,max):
	numstr = str(x)
	sum = x
	test = 0
	for y in range(0,len(numstr)):
		test += (int(numstr[y]))**5
	if test == sum:
		ans += sum
print ans
