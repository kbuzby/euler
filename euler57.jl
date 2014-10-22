count = 0
for x = 2:1000
	t2 = big(1//2)
	for y = 1:x
		t1 = big(2 + t2)
		t2 = big(1/t1)
	end
	number = big(1 + t2)
	if length(string(big(num(number)))) > length(string(big(den(number))))
		count += 1
		println(number)
	end
end
println(count)
