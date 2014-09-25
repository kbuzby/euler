halfwidth = 500
max = (halfwidth + halfwidth + 1)**2
total = 1
num1 = 3
num2 = 5
num3 = 7
num4 = 9
num1add = 10
num2add = 12
num3add = 14
num4add = 16
while num4 <= max :
	total += num1 + num2 + num3 + num4
	num1 += num1add
	num2 += num2add
	num3 += num3add
	num4 += num4add
	num1add += 8
	num2add += 8
	num3add += 8
	num4add += 8

print total
