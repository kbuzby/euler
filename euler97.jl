function modulo(base, exp, digits, mod, at)
	mod = (big(int128(mod^2)))%(10^digits)
	at *= 2
	if at == exp
		return mod
	else
		return big(int128(modulo(base, exp, digits, mod, at)))
	end
end

string = bin(7830457)[end:-1:1]
bins = Int64[]
i = 0
for c in string
	if c  == '1'
		push!(bins,2^i)
	end
	i += 1
end

digits = 10
answer = 512
pmod = 256
pat = 8
for ex = 3:length(bins)
	answer = big(int128((answer*modulo(2,bins[ex],digits,pmod,pat))))%(10^digits)
	println(bins[ex])
	pmod = big(int128(modulo(2,bins[ex],digits,pmod,pat)))
	println(pmod)
	pat = bins[ex]
end
answer *= 28433
answer = answer%(10^digits)
answer += 1
println(answer)
