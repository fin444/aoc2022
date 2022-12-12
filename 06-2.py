line = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()][0]

prev = []

for i in range(len(line)):
	prev.append(line[i])
	if len(prev) == 15:
		prev.pop(0)
		isUnique = True
		for j in range(len(prev)):
			if prev.index(prev[j]) != j:
				isUnique = False
		if isUnique:
			print(i + 1)
			break