F1 = 1
F2 = 1
F3 = F1 + F2
count = 3
while len(str(F3))<1000:
	F1 = F2
	F2 = F3
	F3 = F1 + F2
	count += 1
print count
