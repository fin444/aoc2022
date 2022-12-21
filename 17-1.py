lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

rocks = (
	((0, 0), (1, 0), (2, 0), (3, 0)),
	((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
	((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
	((0, 0), (0, 1), (0, 2), (0, 3)),
	((0, 0), (0, 1), (1, 0), (1, 1))
)
pattern = lines[0]
patternIndex = 0

highest = [-1 for i in range(7)]

filled = set()

def blow(rock):
	global patternIndex
	move = -1 if pattern[patternIndex % len(pattern)] == "<" else 1
	canMove = True
	for r in rock:
		if r[0] + move < 0 or r[0] + move > 6 or (r[0] + move, r[1]) in filled:
			canMove = False
			break
	if canMove:
		for r in rock:
			r[0] += move
	patternIndex += 1

for i in range(2022):
	rock = [[r[0] + 2, r[1] + max(highest) + 4] for r in rocks[i % 5]]
	while True:
		blow(rock)
		canMove = True
		for r in rock:
			if r[1] == 0 or (r[0], r[1] - 1) in filled:
				canMove = False
				break
		if canMove:
			for r in rock:
				r[1] -= 1
		else:
			for r in rock:
				filled.add((r[0], r[1]))
				if highest[r[0]] < r[1]:
					highest[r[0]] = r[1]
			break

print(max(highest) + 1)