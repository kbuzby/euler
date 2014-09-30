def hexagonals(n):
	hex = []
	for x in range(1,n):
		hex.append(x*((2*x)-1))
	return hex

def pentagonals(n):
	pent = []
	for x in range(1,n):
		pent.append(x*((3*x)-1)*0.5)
	return pent

def triagonals(n):
	tri = []
	for x in range(1,n):
		tri.append(x*(x+1)*0.5)
	return tri

limit = 1000000

hexs = hexagonals(limit)
pents = pentagonals(limit)
tris = triagonals(limit)

ans = 0
while ans<3:
	for tri in tris:
		for pent in pents:
			if pent == tri:
				for hex in hexs:
					if hex == pent:
						print tri
						ans += 1
					elif hex > pent:
						break
			elif pent > tri:
				break
