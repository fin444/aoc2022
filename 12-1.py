lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

alphabet = "abcdefghijklmnopqrstuvwxyzSE"

layout = []
start = ()

for line in lines:
	layout.append([])
	for char in line:
		layout[-1].append(char)
		if char == "S":
			start = (len(layout) - 1, len(layout[-1]) - 1)

visited = [start]
paths = [[start]]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def getHeight(goto):
	height = alphabet.index(layout[goto[0]][goto[1]])
	if layout[goto[0]][goto[1]] == "S":
		height = 0
	elif layout[goto[0]][goto[1]] == "E":
		height = 25
	return height

def easyBreak():
	global visited
	global paths
	global dirs
	while True:
		newPaths = []
		visitedThisStep = []
		for i in range(len(paths)):
			path = paths[i]
			outlets = []
			for d in dirs:
				goto = (path[-1][0] + d[0], path[-1][1] + d[1])
				if goto in visited or goto[0] < 0 or goto[0] >= len(layout) or goto[1] < 0 or goto[1] >= len(layout[0]):
					continue
				if getHeight(goto) - 1 > getHeight(path[-1]):
					continue
				if layout[goto[0]][goto[1]] == "E":
					print(len(path))
					return
				outlets.append(goto)
				if goto not in visitedThisStep:
					visitedThisStep.append(goto)
			for j in range(len(outlets)):
				newPaths.append(path + [outlets[j]])
		visited += visitedThisStep
		paths = newPaths
		toRemove = []
		endings = []
		for i in range(len(paths)):
			if paths[i][-1] in endings:
				toRemove.append(i)
			else:
				endings.append(paths[i][-1])
		for i in range(len(toRemove)):
			paths.pop(toRemove[i] - i)

easyBreak()