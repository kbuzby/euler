num = range(0,101)
sum1 = 0
sum2 = 0
for x in num:
	sum1 = sum1 + (x * x)
	sum2 = sum2 + x
sum2 = sum2 * sum2
ans = sum2 - sum1
print ans
