count = 2
for lb in range(0,(200/100)):
	lbsum = lb * 100
	for fifty in range(0,((250-lbsum)/50)):
		fiftysum = fifty * 50
		for twenty in range(0,((220-lbsum-fiftysum)/20)):
			twentysum = twenty * 20
			for ten in range(0,((210-lbsum-fiftysum-twentysum)/10)):
				tensum = ten * 10
				for five in range(0,((205-lbsum-fiftysum-twentysum-tensum)/5)):
					fivesum = five * 5
					for two in range(0,((202-lbsum-fiftysum-twentysum-tensum-fivesum)/2)):
						twosum = two * 2
						for one in range(0,(201-lbsum-fiftysum-twentysum-tensum-fivesum-twosum)):
							numsum = lbsum + fiftysum + twentysum + tensum + fivesum + twosum + one
							if numsum == 200:
								print str(lbsum)+"Xlb "+str(fiftysum)+"X50p "+str(twentysum)+"X20p "+str(tensum)+"X10p "+str(fivesum)+"X5p "+str(twosum)+"X2p "+str(one)+"X1p"
								count +=1
print count
