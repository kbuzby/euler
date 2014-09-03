num = 600851475143
x = 1
isprime=0
while num>0:
	prime = x+1
	for y in range(prime,1,-1):
		if prime%y!=0:
			isprime=1
		else:
			isprime=0
	if isprime==1:
		print prime
		num=num/prime
		print num	
		highprime=prime
		print highprime	
