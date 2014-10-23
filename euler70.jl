function phi(n)
        pf = factor(n)
        y = n
        for x in pf
                y *= 1 - (1/x[1])
        end
        return int(y)
end

function isperm(n,phin)
	phis = []
               ns = []
               for c in "$phin"
                   push!(phis,c)
               end
               for c in "$n"
                   push!(ns,c)
               end
               if length(ns) == length(phis) && sort(ns) == sort(phis)
                   return true
               else
                   return false
               end
       end

minn = 10
ans = 0
for n = 2:9999999
	phin = phi(n)
	t = n/phin
	if t < minn
		if isperm(n,phin)
#			println(n,',',phin)		
			ans = n
			minn = t
		end
	end
end
println(ans)			 
