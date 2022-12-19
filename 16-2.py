lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

usefulValves = {"AA": 0}
paths = {}
usefulPaths = {}

for line in lines:
	if line.split("rate=")[1].split(";")[0] != "0":
		usefulValves[line[6:8]] = int(line.split("rate=")[1].split(";")[0])
	if "valves" in line:
		paths[line[6:8]] = line.split("valves ")[1].split(", ")
	else:
		paths[line[6:8]] = line.split("valve ")[1].split(", ")

for valve in usefulValves:
	visited = [valve]
	usefulPaths[valve] = {}
	depth = 0
	locs = [valve]
	while len(usefulPaths[valve]) < len(usefulValves) - 1:
		depth += 1
		newLocs = []
		for loc in locs:
			for dest in paths[loc]:
				if dest not in visited:
					newLocs.append(dest)
					visited.append(dest)
					if dest in usefulValves:
						usefulPaths[valve][dest] = depth
		locs = newLocs

def search(youLoc, eleLoc, visited, youTime, eleTime):
	if len(visited) == len(usefulValves):
		return 0
	bestPath = 0
	if youTime >= eleTime:
		for dest in usefulPaths[youLoc]:
			if dest not in visited:
				newTime = youTime - usefulPaths[youLoc][dest] - 1
				if newTime > 0:
					s = search(dest, eleLoc, visited + [dest], newTime, eleTime) + (usefulValves[dest] * newTime)
					if s > bestPath:
						bestPath = s
	else:
		for dest in usefulPaths[eleLoc]:
			if dest not in visited:
				newTime = eleTime - usefulPaths[eleLoc][dest] - 1
				if newTime > 0:
					s = search(youLoc, dest, visited + [dest], youTime, newTime) + (usefulValves[dest] * newTime)
					if s > bestPath:
						bestPath = s
	return bestPath

# took 3.5 minutes to run lol
print(search("AA", "AA", ["AA"], 26, 26))