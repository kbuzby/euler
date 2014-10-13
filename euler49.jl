function getprimes(n)
	numbers = [n:-1:2]
	primes = Int64[]
	while !isempty(numbers)
		p = pop!(numbers)
		push!(primes, p)
		numbers = setdiff(numbers, [p*2:p:n+1])
	end
	return primes
end

primes = getprimes(9999)

for prime in primes
	perms = collect(permutations("$prime"))
	temp = 0
	for perm in perms
		if int(perm) > prime && isprime(int(perm))
			temp = int(perm) - prime
			if temp != 0 && isprime(prime + temp) && in("$(prime+temp)",perms) && isprime(prime + (2*temp)) && in("$(prime+(2*temp))",perms)
                		println(prime,(prime+temp),(prime+(2*temp)))
				primes = setdiff(primes,perms)
			end	
		end
	end
end

