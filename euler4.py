test = 0
teststr = ""
pal = 0
for x in range(100,1000):
	for y in range(100,1000):
		test = x*y	
		teststr = str(test)
		if teststr==teststr[::-1]:
			if (test > pal):
				pal = test
				print pal
print x
print y
