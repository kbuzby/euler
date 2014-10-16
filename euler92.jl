function nextnum(n)
	strn = "$n"
	next = 0
	for dig in strn
		next += (int(dig-48))^2
	end
	return next
end

unhappy = [4,16,37,58,89,145,42,20]

count = 0

for n = 2:9999999
	chain = nextnum(n)
	while !in(chain,unhappy) && chain != 1
		chain = nextnum(chain)
	end
	if chain == 1
		continue
	elseif in(chain,unhappy)
		count += 1
	end
end
println(count)
