lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

drops = set()
sides = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
dimensions = [0, 0, 0]

for line in lines:
	l = line.split(",")
	d = (int(l[0]), int(l[1]), int(l[2]))
	drops.add(d)
	if d[0] > dimensions[0]:
		dimensions[0] = d[0]
	if d[1] > dimensions[1]:
		dimensions[1] = d[1]
	if d[2] > dimensions[2]:
		dimensions[2] = d[2]

dimensions[0] += 1
dimensions[1] += 1
dimensions[2] += 1
steam = set()
count = 0

curr = [(0, 0, 0)]
nex = []
while len(curr) > 0:
	for pos in curr:
		steam.add(pos)
		for side in sides:
			s = (pos[0] + side[0], pos[1] + side[1], pos[2] + side[2])
			if s[0] > dimensions[0] or s[0] < -1 or s[1] > dimensions[1] or s[1] < -1 or s[2] > dimensions[2] or s[2] < -1:
				continue
			if s in steam:
				continue
			if s in drops:
				count += 1
			elif s not in nex:
				nex.append(s)
	curr = nex
	nex = []

print(count)