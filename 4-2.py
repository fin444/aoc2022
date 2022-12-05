lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

count = 0

for line in lines:
	first = line.split(",")[0]
	second = line.split(",")[1]
	firstRange = [int(first.split("-")[0]), int(first.split("-")[1])]
	secondRange = [int(second.split("-")[0]), int(second.split("-")[1])]
	if (firstRange[0] <= secondRange[0] and firstRange[1] >= secondRange[0]) or (firstRange[0] <= secondRange[1] and firstRange[1] >= secondRange[1]):
		count += 1
	elif (secondRange[0] <= firstRange[0] and secondRange[1] >= firstRange[0]) or (secondRange[0] <= firstRange[1] and secondRange[1] >= firstRange[1]):
		count += 1

print(count)