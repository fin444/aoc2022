lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]
visible = []

for i in range(len(lines)):
	highest = -1
	for j in range(len(lines[0])):
		if highest < int(lines[i][j]):
			highest = int(lines[i][j])
			if (i, j) not in visible:
				visible.append((i, j))
	highest = -1
	for j in reversed(range(len(lines[0]))):
		if highest < int(lines[i][j]):
			highest = int(lines[i][j])
			if (i, j) not in visible:
				visible.append((i, j))

for j in range(len(lines[0])):
	highest = -1
	for i in range(len(lines)):
		if highest < int(lines[i][j]):
			highest = int(lines[i][j])
			if (i, j) not in visible:
				visible.append((i, j))
	highest = -1
	for i in reversed(range(len(lines))):
		if highest < int(lines[i][j]):
			highest = int(lines[i][j])
			if (i, j) not in visible:
				visible.append((i, j))

print(visible)
print(len(visible))