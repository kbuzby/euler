

# Below code works for example case, but takes too long for problem
curmax = 2/5
for d = 1000000:-1:2, n = (int(d*(3/7))):-1:1
    if curmax < (n/d) < (3/7)
        if gcd(n,d) == 1 && round(n/d,7) == (round(3/7,7)-0.0000001)
            println(n//d)
            curmax = n/d
            break
        end
    end
end
#sol = sort(sol)
#println(sol[( findfirst(sol,(3//7)) ) - 1 ])
