
rng = 2:1000000
sol = []
for d = rng, n = 1:d
    if gcd(n,d) == 1
        push!(sol,n//d)
    end
end
println(length(sol))
