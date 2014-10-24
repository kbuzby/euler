function minpath(cost, m, n)
        tc = Array(Int64,m,n)
        tc[1,1] = int(cost[1,1])
        for i = 2:m
                tc[i,1] = tc[i-1,1] + int(cost[i,1])
        end
        for j = 2:n
                tc[1,j] = tc[1,j-1] + int(cost[1,j])
        end
        for i = 2:m, j = 2:n
                tc[i,j] = min(tc[i,j-1],tc[i-1,j]) + int(cost[i,j])
		println(tc[i,j])
        end
        return tc[m,n]
end


f = open("p081_matrix.txt")
rl = readlines(f)
x = 1
arr = [131 673 234 103 18;201 96 342 965 150; 630 803 746 422 111; 537 699 497 121 956; 805 732 524 37 331]

println(minpath(arr,5,5))
