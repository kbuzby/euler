perms = collect(permutations("0123456789"))
sum = 0
for perm in perms
	if int(perm[2:4])%2 == 0 && int(perm[3:5])%3 == 0 && int(perm[4:6])%5==0 && int(perm[5:7])%7==0 && int(perm[6:8])%11==0 && int(perm[7:9])%13==0 && int(perm[8:10])%17==0
		sum += int(perm)
	end
end
println(sum)
