lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]
visited = [(0, 0)]
head = [0, 0]
tails = [[0, 0] for i in range(9)]

for num in range(len(lines)):
	line = lines[num]
	for j in range(int(line[2:])):
		if line[0] == "U":
			head[0] += 1
		elif line[0] == "D":
			head[0] -= 1
		elif line[0] == "L":
			head[1] -= 1
		elif line[0] == "R":
			head[1] += 1
		for i in range(len(tails)):
			tail = tails[i]
			prev = []
			if i == 0:
				prev = head
			else:
				prev = tails[i - 1]
			oldtail = tail
			if abs(prev[0] - tail[0]) > 1 or abs(prev[1] - tail[1]) > 1:
				if abs(prev[0] - tail[0]) == abs(prev[1] - tail[1]):
					if prev[0] > tail[0]:
						tails[i] = [prev[0] - 1, prev[1]]
					else:
						tails[i] = [prev[0] + 1, prev[1]]
					if prev[1] > tail[1]:
						tails[i][1] -= 1
					else:
						tails[i][1] += 1
				elif abs(prev[0] - tail[0]) > abs(prev[1] - tail[1]):
					if prev[0] > tail[0]:
						tails[i] = [prev[0] - 1, prev[1]]
					else:
						tails[i] = [prev[0] + 1, prev[1]]
				else:
					if prev[1] > tail[1]:
						tails[i] = [prev[0], prev[1] - 1]
					else:
						tails[i] = [prev[0], prev[1] + 1]
		if (tails[8][0], tails[8][1]) not in visited:
			visited.append((tails[8][0], tails[8][1]))

print(len(visited))