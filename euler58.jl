d1 = 3
d2 = 5
d3 = 7
d4 = 9
count = 4
pc = 3
r = pc/count
dim = (count/2) + 1
n = 10
while r > 0.1
	d1 += n
	d2 += n+2
	d3 += n+4
	d4 += n+6
	count += 4
	if isprime(d1)
		pc += 1
	end
	if isprime(d2)
		pc += 1
	end
	if isprime(d3)
		pc += 1
	end
	if isprime(d4)
		pc += 1
	end	
	r = pc/count
	n += 8
	dim = (count/2) + 1
end
println(dim)
