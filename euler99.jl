f = open("p099_base_exp.txt")
lines = readdlm(f,'\n',String)

x = 0
n = 1
ans = 1
for line in lines
	subline = split(line,',')
	if int(subline[2])*log(int(subline[1])) > x
		ans = n
		x = int(subline[2])*log(int(subline[1]))
	end
	n += 1
end
println(ans)
