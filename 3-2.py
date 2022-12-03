lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

scores = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0

for i in range(0, int(len(lines) / 3)):
	j = i * 3
	for char in lines[j]:
		if lines[j + 1].__contains__(char) and lines[j + 2].__contains__(char):
			count += scores.index(char)
			break

print(count)