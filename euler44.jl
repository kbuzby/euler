function pent(n)
	p = (n*((3*n)-1))/2
	return p
end

function ispent(n)
	number = ((((24*n)+1)^0.5)+1)/6
	return isinteger(number)
end

result = 0
found = false
i = 1

while !found
	i += 1
	x = pent(i)
	for j = i-1:-1:1
		y = pent(j)
		if ispent(x - y) && ispent(x + y)
			result = abs(y - x)
			found = true
			break
		end
	end
end
println(int(result))
