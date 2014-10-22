function phi(n)
	pf = factor(n)
	y = n
	for x in pf
		y *= 1 - (1/x[1])
	end
	return y
end

ans = 0
max = 0
for n = 1:1000000
	t = n / phi(n)
	if t > max
		max = t
		ans = n
	end
end
println(ans)
