lower = 0
result = 0
n = 1.0
while lower<10
	lower = ceil(10^((n-1.0)/n))
	result += 10-lower
	n += 1
end
println(result)
