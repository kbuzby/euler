function pf(n)
	return length(factor(n))
end

n = 1
while true
	if  pf(n) == 4 && pf(n+1) == 4 && pf(n+2) == 4 && pf(n+3) == 4
		println(n)
		break
	else
		n += 1
	end
end
