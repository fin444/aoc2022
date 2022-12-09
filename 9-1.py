lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]
visited = [(0, 0)]
head = [0, 0]
tail = [0, 0]

for line in lines:
	for i in range(int(line[2:])):
		if line[0] == "U":
			head[0] += 1
		elif line[0] == "D":
			head[0] -= 1
		elif line[0] == "L":
			head[1] -= 1
		elif line[0] == "R":
			head[1] += 1
		if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
			tail = [head[0], head[1]]
			if line[0] == "U":
				tail[0] -= 1
			elif line[0] == "D":
				tail[0] += 1
			elif line[0] == "L":
				tail[1] += 1
			elif line[0] == "R":
				tail[1] -= 1
			if (tail[0], tail[1]) not in visited:
				visited.append((tail[0], tail[1]))

print(len(visited))