from num2words import num2words

def letter(num):
	count = 0
	for char in num:
		if char.isalpha():
			count += 1
	return count

total = 0

for x in range(1,1001):
	words = num2words(x)
	total += letter(words)
print total
