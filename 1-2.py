lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

most1 = 0
most2 = 0
most3 = 0
curr = 0

for line in lines:
	if line == "":
		if curr > most1:
			most3 = most2
			most2 = most1
			most1 = curr
		elif curr > most2:
			most3 = most2
			most2 = curr
		elif curr > most3:
			most3 = curr
		curr = 0
	else:
		curr += int(line)

print(most1 + most2 + most3)