total = 0
for x in range(1,1001):
	total += x**x
totalstr = str(total)
print totalstr[len(totalstr)-10:len(totalstr)]
