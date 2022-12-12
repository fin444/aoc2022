lines = [line.replace("\n", "") for line in open("aoc_input.txt", "r").readlines()]

score = 0

for line in lines:
	roundscore = 0
	attack = line.split(" ")[0]
	defend = line.split(" ")[1]
	if attack == "A":
		if defend == "X":
			roundscore += 3
		elif defend == "Y":
			roundscore += 6
		elif defend == "Z":
			roundscore += 0
	elif attack == "B":
		if defend == "X":
			roundscore += 0
		elif defend == "Y":
			roundscore += 3
		elif defend == "Z":
			roundscore += 6
	elif attack == "C":
		if defend == "X":
			roundscore += 6
		elif defend == "Y":
			roundscore += 0
		elif defend == "Z":
			roundscore += 3
	
	if defend == "X":
		roundscore += 1
	elif defend == "Y":
		roundscore += 2
	elif defend == "Z":
		roundscore += 3
	
	score += roundscore

print(score)