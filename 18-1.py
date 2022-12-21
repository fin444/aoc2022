lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

drops = set()
sides = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

for line in lines:
	l = line.split(",")
	drops.add((int(l[0]), int(l[1]), int(l[2])))

count = 0

for drop in drops:
	for side in sides:
		if (drop[0] + side[0], drop[1] + side[1], drop[2] + side[2]) not in drops:
			count += 1

print(count)