num = 1
den = 1
for i = 1:9, j = 1:9, m = 1:9, n = 1:9 
	if int("$i$j")/int("$m$n") < 1 && ((j == m && int("$i$j")/int("$m$n") == i/n) || (i == m && int("$i$j")/int("$m$n") == j/m)) 
		num *= int("$i$j")
		den *= int("$m$n")
		println("$num/$den")
	end
end
