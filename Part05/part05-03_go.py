# Write your solution here
def who_won(game_boar: list):
	p1: int = 0
	p2: int = 0

	for r in range(len(game_boar)):
		for c in game_boar[r]:
			if c == 1:
				p1 += 1
			if c == 2:
				p2 += 1

	if p1 > p2:
		return 1
	elif p1 < p2:
		return 2
	else:
		return 0


if __name__ == "__main__":
	# board=[[2,2,1,2,2,1],[1,1,1,1,2,1],[2,1,0,0,2,2],[1,2,0,2,0,2],[2,2,1,2,0,1],[1,2,1,1,1,1],[1,2,1,2,1,1],[2,2,2,1,2,2],[2,1,1,1,1,2],[1,0,0,2,0,1]]
	board= [[1, 2, 2, 2], [2, 1, 1, 1], [0, 2, 1, 0]]
	print(who_won(board))
