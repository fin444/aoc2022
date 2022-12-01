lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

most = 0
curr = 0

for line in lines:
	if line == "":
		if curr > most:
			most = curr
		curr = 0
	else:
		curr += int(line)

print(most)