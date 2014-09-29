num = '.'
for x in range(1,500000):
	num += str(x)

print int(num[1]) * int(num[10]) * int(num[100]) * int(num[1000]) * int(num[10000]) * int(num[100000]) * int(num[1000000])
