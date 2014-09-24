def alphavalue(alpha):
	if alpha == "A":
		return 1
	elif alpha == "B":
		return 2
	elif alpha == "C":
		return 3
	elif alpha == "D":
		return 4
	elif alpha == "E":
		return 5
	elif alpha == "F":
		return 6
	elif alpha == "G":
		return 7
	elif alpha == "H":
		return 8
	elif alpha == "I":
		return 9
	elif alpha == "J":
		return 10
	elif alpha == "K":
		return 11
	elif alpha == "L":
		return 12
	elif alpha == "M":
		return 13
	elif alpha == "N":
		return 14
	elif alpha == "O":
		return 15
	elif alpha == "P":
		return 16
	elif alpha == "Q":
		return 17
	elif alpha == "R":
		return 18
	elif alpha == "S":
		return 19
	elif alpha == "T":
		return 20
	elif alpha == "U":
		return 21	
	elif alpha == "V":
		return 22
	elif alpha == "W":	
		return 23
	elif alpha == "X":
		return 24
	elif alpha == "Y":
		return 25
	elif alpha == "Z":
		return 26
names = []
with open('p022_names.txt') as csvfile:
	for line in csvfile:
		names = line.split(",")
names = sorted(names)
total = 0
for x in range(0,len(names)):
	namevalue = 0
	name = names[x].upper()
	for y in range(1,len(name)-1):
		lettervalue = alphavalue(name[y])
		namevalue += lettervalue
	total += (x+1) * namevalue
print total
