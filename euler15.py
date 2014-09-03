n = 6

def find_all_paths(graph,start,end,path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if not graph.has_key(start):
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = find_all_paths(graph,node,end,path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths


graph = {}
for x in range(0,n+1):
	for y in range(0,n+1):
		if (x == n and y == n):
			graph[str(x).zfill(2)+str(y).zfill(2)] = ['none']
		elif (x==n):
			graph[str(x).zfill(2)+str(y).zfill(2)] = [str(x).zfill(2)+str(y+1).zfill(2)]
		elif (y==n):
			graph[str(x).zfill(2)+str(y).zfill(2)] = [str(x+1).zfill(2)+str(y).zfill(2)]

		else:
			graph[str(x).zfill(2)+str(y).zfill(2)] = [str(x+1).zfill(2)+str(y).zfill(2), str(x).zfill(2)+str(y+1).zfill(2)]

result = find_all_paths(graph, '0000', str(n).zfill(2)+str(n).zfill(2))	
print len(result)
