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

def gettris(n):
	tris = []
	for val in range(1,n):
		num = ((0.5) * val * (val+1))
		print num
		tris.append(num)
	return tris

triangles = gettris(100)
print triangles
words = []
with open('p042_words.txt') as csvfile:
	for line in csvfile:
		words = line.split(",")
total = 0

for word in words:
	wordvalue = 0
	for x in range(1,len(word)-1):
		lettervalue = alphavalue(word[x])
		wordvalue += lettervalue
	if wordvalue in triangles:
		total += 1
print total
