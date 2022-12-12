lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

state = 0
stacks = [[] for i in range(9)]

for line in lines:
	if state == 0:
		if line == "":
			state = 1
			for stack in stacks:
				if len(stack) != 0:
					stack.pop()
					stack.reverse()
		else:
			for i in range(0, len(line)):
				if not (line[i] == "[" or line[i] == "]" or line[i] == " "):
					stacks[int((i - 1) / 4)].append(line[i])
	else:
		for i in range(int(line.split("move ")[1].split(" from")[0])):
			if len(stacks[int(line[-6]) - 1]) != 0:
				stacks[int(line[-1]) - 1].append(stacks[int(line[-6]) - 1].pop())

print(stacks)