# (b/t)*((b-1)/(t-1)) = 0.5
# b(b-1) = 0.5(t(t-1))

function euler100(t)
    for br = Int64(0.7*t):Int64(0.71*t)
        tmap = round(br/((t^2)-t),5)
        if tmap == 0.5
            return br
        end
    end
    return 0
end

t = 10^12
sol = euler100(t)
while sol == 0
    t += 1
    sol = euler100(t)
end
println(sol)

