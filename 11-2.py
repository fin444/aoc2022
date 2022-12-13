import math

lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

monkeyItems = []
monkeyOps = []
monkeyTests = []

numItems = 0
magicMod = 1

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
			numItems += 1
	elif line.startswith("  Operation:"):
		monkeyOps[currMonkey].append(line[23])
		monkeyOps[currMonkey].append(line[25:])
	elif line.startswith("  Test:"):
		monkeyTests[currMonkey].append(int(line[21:]))
		magicMod *= int(line[21:])
	elif line.startswith("    If true:"):
		monkeyTests[currMonkey].append(int(line[29:]))
	elif line.startswith("    If false:"):
		monkeyTests[currMonkey].append(int(line[30:]))

monkeys = [0 for i in range(len(monkeyItems))]

for monkey in range(len(monkeys)):
	while len(monkeyItems[monkey]) < numItems:
		monkeyItems[monkey].append(-1)

for i in range(10000):
	for monkey in range(len(monkeys)):
		for item in range(numItems):
			if monkeyItems[monkey][item] == -1:
				break
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
			# shrink
			monkeyItems[monkey][item] = monkeyItems[monkey][item] % magicMod
			# test
			if monkeyItems[monkey][item] % monkeyTests[monkey][0] == 0:
				for j in range(numItems):
					if monkeyItems[monkeyTests[monkey][1]][j] == -1:
						monkeyItems[monkeyTests[monkey][1]][j] = monkeyItems[monkey][item]
						break
			else:
				for j in range(numItems):
					if monkeyItems[monkeyTests[monkey][2]][j] == -1:
						monkeyItems[monkeyTests[monkey][2]][j] = monkeyItems[monkey][item]
						break
		for j in range(numItems):
			monkeyItems[monkey][j] = -1

print(sorted(monkeys)[-1] * sorted(monkeys)[-2])