mynum = 1
max = 0
while true
	n = 1
	pand = ""
	while length(pand)<9
		pand = "$pand$(mynum*n)"
		n .+= 1		
	end

	if length(pand)==9
		temp = ""

		for c in pand
			if search(temp, c) == 0
				temp = "$temp$c"
			else 
				break
			end
		end

		if int(temp)>max && search(temp, '0')==0
			max = int(temp) 
			println(max)
		end
	end

	mynum .+= 1
	


	if length("$mynum")>5
		break
	end
end
