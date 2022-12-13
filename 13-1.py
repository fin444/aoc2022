lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

total = 0

def compare(left, right):
	for i in range(len(left)):
		if i >= len(right):
			return False
		if type(left[i]) == int and type(right[i]) == int:
			if left[i] > right[i]:
				return False
			elif left[i] < right[i]:
				return True
		else:
			l = left[i]
			r = right[i]
			if type(l) == int:
				l = [l]
			if type(r) == int:
				r = [r]
			result = compare(l, r)
			if result != "inconclusive":
				return result
	if len(left) < len(right):
		return True
	return "inconclusive"

for i in range(len(lines) // 3):
	left = eval(lines[i * 3])
	right = eval(lines[i * 3 + 1])
	if compare(left, right):
		total += i + 1

print(total)