lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

scores = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0

for line in lines:
	first = line[0:int(len(line) / 2)]
	second = line[int(len(line) / 2):]
	for char in first:
		if second.__contains__(char):
			count += scores.index(char)
			break

print(count)