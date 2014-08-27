x = 20
y = range(1,21)
count = 0
while count!=20:
	count = 0
	x = x+20
	for i in y:
		if x%i==0:
			count = count+1
print x
