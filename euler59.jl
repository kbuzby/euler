function encrypt(str,key)
	n = 1
	nstr = ""
	for c in str
		if n > 3
			n = 1
		end
		nstr = string(nstr,char(int(c)$int(key[n])))	
		n += 1
	end
	return nstr
end

f = open("p059_cipher.txt")
cipher = readdlm(f,',',Int64)
str = ""
for i in cipher
	str = "$str$(char(i))"
end
ans = ""
prevc = 0
for a = 97:122, b = 97:122, c = 97:122
	key = string(char(a),char(b),char(c))
	text = encrypt(str,key)
	count = length(findin(text," "))
	if count > prevc
		ans = text
		prevc = count
	end
end
tsum = 0
for c in ans
	tsum += int(c)
end
println(tsum)
