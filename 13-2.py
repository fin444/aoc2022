lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

packets = [[[2]], [[6]]]
biggestKey = 0
magnitude = 1

def realList(packet):
	if len(packet) == 0:
		return [0]
	l = []
	for p in packet:
		if type(p) == int:
			l.append(p)
		else:
			l += realList(p)
	return l

def key(packet):
	l = realList(packet)
	s = 0
	for i in l:
		s *= 10
		if i == 0:
			s += 1
		elif i == 10:
			s += 9
		else:
			s += i
	while s < magnitude and s != 0:
		s *= 10
	return s

for line in lines:
	if line != "":
		packets.append(eval(line))

for p in packets:
	k = key(p)
	if k > biggestKey:
		biggestKey = k

while biggestKey > magnitude:
	magnitude *= 10

packets.sort(key=key)

print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))