lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

dirs = {"/": {}}
path = ["/"]

for line in lines:
	if line.startswith("$ ls"):
		pass
	elif line.startswith("$ cd"):
		if line == "$ cd /":
			path = ["/"]
		elif line == "$ cd ..":
			if len(path) > 1:
				path.pop()
		else:
			d = dirs
			for i in path:
				d = d[i]
			d[line[5:]] = {}
			path.append(line[5:])
	else:
		d = dirs
		for i in path:
			d = d[i]
		if line.startswith("dir"):
			d[line.split(" ")[1]] = {}
		else:
			size = int(line.split(" ")[0])
			name = line.split(" ")[1]
			d[name] = size

total = 0

def recursion(d):
	global total
	totalsize = 0
	for child in d:
		size = 0
		if type(d[child]) is dict:
			size = recursion(d[child])
			if size < 100000:
				total += size
		else:
			size = d[child]
		totalsize += size
	return totalsize

recursion(dirs)

print(total)