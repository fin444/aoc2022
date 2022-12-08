lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]
bestscore = 0

for i in range(len(lines)):
	for j in range(len(lines[0])):
		height = int(lines[i][j])
		score = 1
		count = 0
		# up
		for k in reversed(range(0, i)):
			count += 1
			if int(lines[k][j]) >= height:
				break
		score *= count
		count = 0
		# down
		for k in range(i + 1, len(lines)):
			count += 1
			if int(lines[k][j]) >= height:
				break
		score *= count
		count = 0
		# up
		for k in reversed(range(0, j)):
			count += 1
			if int(lines[i][k]) >= height:
				break
		score *= count
		count = 0
		# down
		for k in range(j + 1, len(lines[0])):
			count += 1
			if int(lines[i][k]) >= height:
				break
		score *= count
		if bestscore < score:
			bestscore = score

print(bestscore)