import math

lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

monkeyItems = []
monkeyOps = []
monkeyTests = []

currMonkey = -1
for line in lines:
	if line.startswith("Monkey "):
		currMonkey += 1
		monkeyItems.append([])
		monkeyOps.append([])
		monkeyTests.append([])
	elif line.startswith("  Starting items:"):
		for i in line[18:].split(", "):
			monkeyItems[currMonkey].append(int(i))
	elif line.startswith("  Operation:"):
		monkeyOps[currMonkey].append(line[23])
		monkeyOps[currMonkey].append(line[25:])
	elif line.startswith("  Test:"):
		monkeyTests[currMonkey].append(int(line[21:]))
	elif line.startswith("    If true:"):
		monkeyTests[currMonkey].append(int(line[29:]))
	elif line.startswith("    If false:"):
		monkeyTests[currMonkey].append(int(line[30:]))

monkeys = [0 for i in range(len(monkeyItems))]

for i in range(20):
	for monkey in range(len(monkeys)):
		for item in range(len(monkeyItems[monkey])):
			monkeys[monkey] += 1
			# monkey operations
			other = 0
			if monkeyOps[monkey][1] == "old":
				other = monkeyItems[monkey][item]
			else:
				other = int(monkeyOps[monkey][1])
			if monkeyOps[monkey][0] == "+":
				monkeyItems[monkey][item] += other
			else:
				monkeyItems[monkey][item] *= other
			# boredom
			monkeyItems[monkey][item] = math.floor(monkeyItems[monkey][item] / 3)
			# test
			if monkeyItems[monkey][item] % monkeyTests[monkey][0] == 0:
				monkeyItems[monkeyTests[monkey][1]].append(monkeyItems[monkey][item])
			else:
				monkeyItems[monkeyTests[monkey][2]].append(monkeyItems[monkey][item])
		monkeyItems[monkey] = []

print(sorted(monkeys)[-1] * sorted(monkeys)[-2])