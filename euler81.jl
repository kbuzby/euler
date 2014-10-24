function minpath(cost, m, n)
	tc = Array(Int64,length(cost),length(cost))
	tc[1,1] = int(cost[1][1])
	for i = 2:m
		tc[i,1] = tc[i-1,1] + int(cost[i][1])
	end
	for j = 2:n
		tc[1,j] = tc[1,j-1] + int(cost[1][j])
	end
	for i = 2:m, j = 2:n
		tc[i,j] = min(tc[i,j-1],tc[i-1,j]) + int(cost[i][j])
	end
	return tc[m,n]
end

f = open("p081_matrix.txt")
rl = readlines(f)
x = 1

arr = []
for line in rl
	push!(arr,split(strip(line,'\n'),','))
	x += 1
end	


println(minpath(arr,80,80))

#minpath = int(arr[80][80])
#i = 80
#j = 80
#while i !=1 || j != 1	
#	if i != 1 && j != 1
#		if int(arr[i-1][j])<int(arr[i][j-1])
#			println(int(arr[i-1][j]),'<',int(arr[i][j-1]))	
#			i -= 1
#		else
#			println(int(arr[i][j-1]),'<',int(arr[i-1][j]))
#			j -= 1
#		end
#	elseif i == 1
#		j -= 1
#	elseif j == 1
#		i -= 1
#	end
#	println(i,',',j)
#	minpath += int(arr[i][j])
#end 

#println(minpath)
