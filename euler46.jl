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

i = 9
while true
	if !isprime(i)
	gb = false
	primes = getprimes(i)
	for prime in primes, x = 1:i
		if i == prime + (2 * (x^2))
			gb = true

			break
		elseif i < prime + (2*(x^2))
			continue
		end
	end
	if !gb
		println(i)
		break
	end
	end
	i += 2
end	
