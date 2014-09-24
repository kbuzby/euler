tri = [[int(n) for n in s.split()] for s in open('p067_triangle.txt').readlines()]

for row in range(len(tri)-1, 0, -1):
	for col in range(0,row):
		tri[row-1][col] += max(tri[row][col], tri[row][col+1])

print tri[0][0]

#print tri

