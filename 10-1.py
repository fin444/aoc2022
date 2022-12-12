lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

cycle = 0
X = 1
total = 0

def checkInteresting():
	global cycle
	global X
	global total
	if (cycle - 20) % 40 == 0:
		total += X * cycle

for line in lines:
	cycle += 1
	checkInteresting()
	if line.startswith("addx "):
		cycle += 1
		checkInteresting()
		X += int(line[5:])

print(total)