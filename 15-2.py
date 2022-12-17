lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

sensors = []
boundary = 4000000
dirs = [(1, 1)]

for line in lines:
	s = line.split(" ")
	sensor = [int(s[2][2:-1]), int(s[3][2:-1])]
	beacon = [int(s[8][2:-1]), int(s[9][2:])]
	radius = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
	sensors.append([sensor[0], sensor[1], radius])

def count(point, d):
	point[0] += d[0]
	point[1] += d[1]
	if point[0] < 0 or point[0] > boundary or point[1] < 0 or point[1] > boundary:
		return
	for sensor in sensors:
		if abs(point[0] - sensor[0]) + abs(point[1] - sensor[1]) <= sensor[2]:
			return
	print(point[0] * 4000000 + point[1])

for sensor in sensors:
	point = [sensor[0] - sensor[2] - 1, sensor[1]]
	for d in dirs:
		count(point, d)
		while point[0] != sensor[0] and point[1] != sensor[1]:
			count(point, d)

# 02:08:41 already