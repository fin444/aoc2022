lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

covered = []
row = 2000000

for line in lines:
	s = line.split(" ")
	sensor = [int(s[2][2:-1]), int(s[3][2:-1])]
	beacon = [int(s[8][2:-1]), int(s[9][2:])]
	radius = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
	if abs(row - sensor[1]) <= radius:
		covered.append([sensor[0] - (radius - abs(row - sensor[1])), sensor[0] + (radius - abs(row - sensor[1]))])
		
joined = []

while len(covered) > 0:
	lowest = [99999999, 0]
	for r in covered:
		if r[0] < lowest[0]:
			lowest = r
	covered.remove(lowest)
	while True:
		remove = 0
		for r in covered:
			if r[0] <= lowest[1]:
				remove = r
				if r[1] > lowest[1]:
					lowest[1] = r[1]
		if remove == 0:
			break
		else:
			covered.remove(remove)
	joined.append(lowest)

total = 0
for j in joined:
	total += j[1] - j[0] + 1

print(total) # manually subtract number of beacons in row