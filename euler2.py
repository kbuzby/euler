ans = 0
current = 2
past = 1
next = 0

while current <=4000000:
	next = current + past
	if (next%2==0):
		ans=ans+next
	past = current
	current = next
	print next

