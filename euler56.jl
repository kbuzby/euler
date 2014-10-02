max = 0

for a = big(99:-1:1), b = big(99:-1:1)
	numstr = "$(a^b)"
	val = 0
	for c in numstr
		val += (int(c)-48)
		if val > max
			max = val
			println(max)
		end
	end	
end
