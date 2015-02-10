for a = 0:9, b = 0:9, c = 0:9, d = 0:9, e = 0:9, f = 0:9, g = 0:9, h = 0:9, i = 0:9
    if isinteger(sqrt(int("1$(a)2$(b)3$(c)4$(d)5$(e)6$(f)7$(g)8$(h)9$(i)0")))
        println("1$(a)2$(b)3$(c)4$(d)5$(e)6$(f)7$(g)8$(h)9$(i)0")
        break
    end
end    
