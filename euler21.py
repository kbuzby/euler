def d(a):
	total = 0
	for x in range(1,a):
		if a%x == 0:
			total += x
	return total

result = 0
x = 2
while x < 10000:
	num1 = x
	num2 = d(x)
	if num1 == d(num2) and num2 == d(num1) and  num1 != num2:
		result += num1 + num2
		x = max(num1, num2)
		print str(num1) + ' ' + str(num2) + ' ' + str(result)
	x+=1
