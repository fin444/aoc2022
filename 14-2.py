lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

filled = []
lowest = 1

for line in lines:
	points = line.split(" -> ")
	for i in range(1, len(points)):
		prev = [int(points[i - 1].split(",")[0]), int(points[i - 1].split(",")[1])]
		curr = [int(points[i].split(",")[0]), int(points[i].split(",")[1])]
		if curr[1] >= lowest:
			lowest = curr[1] + 1
		while prev[0] != curr[0] or prev[1] != curr[1]:
			point = (prev[0], prev[1])
			if point not in filled:
				filled.append(point)
			if prev[0] == curr[0]:
				if prev[1] > curr[1]:
					prev[1] -= 1
				else:
					prev[1] += 1
			else:
				if prev[0] > curr[0]:
					prev[0] -= 1
				else:
					prev[0] += 1
		filled.append((curr[0], curr[1]))

counter = 1
lastRow = [500]
depth = 1

while depth <= lowest:
	thisRow = []
	for i in range(500 - depth, 501 + depth):
		if (i - 1 in lastRow or i in lastRow or i + 1 in lastRow) and (i, depth) not in filled:
			thisRow.append(i)
			counter += 1
	depth += 1
	lastRow = thisRow

print(counter)