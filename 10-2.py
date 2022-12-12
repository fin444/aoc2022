lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

cycle = 0
X = 1
crt = ""

def checkInteresting():
	global cycle
	global X
	global crt
	if (cycle % 40) - 1 <= X and (cycle % 40) + 1 >= X:
		crt += "#"
	else:
		crt += "."

for line in lines:
	checkInteresting()
	cycle += 1
	if line.startswith("addx "):
		checkInteresting()
		cycle += 1
		X += int(line[5:])

while len(crt) < 240:
	crt += "."

print(crt[0:40])
print(crt[40:80])
print(crt[80:120])
print(crt[120:160])
print(crt[160:200])
print(crt[200:240])