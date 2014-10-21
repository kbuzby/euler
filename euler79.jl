f = open("p079_keylog.txt")
keys = readdlm(f,'\n',String)
println(keys)
pass = ['1','2','3','6','7','8','9','0']
for key in keys
	keyin1 = findin(pass,key[1])[1]
	keyin2 = findin(pass,key[2])[1]
	keyin3 = findin(pass,key[3])[1]
	if keyin1 > keyin2 && keyin1 < keyin3 #if first is greater than second but not third
		insert!(pass,keyin2,key[1])
		deleteat!(pass,keyin1+1)
	elseif keyin1 > keyin2 && keyin1 > keyin3 #if first is greater than second and third
		if keyin2 > keyin3 # if second is greater than third
			#move key 2 before key 3
			insert!(pass,keyin3,key[2])
			deleteat!(pass,keyin2+1)
			keyin1 = findin(pass,key[1])[1]
			keyin2 = findin(pass,key[2])[1]
		end
		#move key 1 before new key 2
		insert!(pass,keyin2,key[1])
		deleteat!(pass,keyin1+1)
	elseif keyin1 < keyin2 && keyin2 > keyin3 #if 1st is ok, but second is greater than third
		#move key2 before key3
		insert!(pass,keyin3,key[2])
		deleteat!(pass,keyin2+1)
	end
	println(pass)
end
println(pass) 
			
