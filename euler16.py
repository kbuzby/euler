power = 1000
digits = 2 ** power
result = 0 
for x in range (0,len(str(digits))):
	result += int((str(digits)[x]))
print result
