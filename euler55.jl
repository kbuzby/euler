function ispalindrome(n)
	strn = "$n"
	revstr = strn[end:-1:1]
	if strn == revstr
		return true
	end
	return false
end

function lychrel(n, count=0)
               strn = "$n"
               revstr = strn[end:-1:1]
               revn = big(int128(revstr))
               if count > 50
                       return true
               end

               if ispalindrome(big(int128(n+revn)))
                       return false
               else
                       count += 1
                       lychrel(big(int128(n+revn)),count)
               end
       end
	

myans = 0
for i = 1:10000
	if lychrel(int128(i))
		myans += 1
		println(i)
	end
end
println(myans)
