import math
digits = math.factorial(100)
result = 0 
for x in range (0,len(str(digits))):
	result += int((str(digits)[x]))
print result
