# Write your solution here
def sudoku_grid_correct(sudoku: list):
	length = len(sudoku)

	for cell in range(length):
		if not row_correct(sudoku, cell) or not column_correct(sudoku, cell):
			return False

	squares: list = [0, 3, 6]
	for sl in squares:
		for sh in squares:
			if not block_correct(sudoku, sl, sh):
				return False

	return True


def block_correct(sudoku: list, row_no: int, column_no: int):
	numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for n in numbers:
		rep: int = 0
		for r in range(row_no, row_no+3):
			for c in range(column_no, column_no+3):
				if sudoku[r][c] == n:
					rep += 1
					if rep > 1:
						return False
	return True


def row_correct(sudoku: list, row_no: int):
	numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for n in numbers:
		rep: int = 0
		for r in sudoku[row_no]:
			if r == n:
				rep += 1
				if rep > 1:
					return False
	return True


def column_correct(sudoku: list, column: int):
	numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for n in numbers:
		rep: int = 0

		for c in range(len(sudoku)):
			if sudoku[c][column] == n:
				rep += 1
				if rep > 1:
					return False
	else:
		return True


if __name__ == "__main__":
	sudoku_1: list = [
					[9, 0, 0, 0, 8, 0, 3, 0, 0],
					[2, 0, 0, 2, 5, 0, 7, 0, 0],
					[0, 2, 0, 3, 0, 0, 0, 0, 4],
					[2, 9, 4, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 7, 3, 0, 5, 6, 0],
					[7, 0, 5, 0, 6, 0, 4, 0, 7],
					[0, 0, 7, 8, 0, 3, 9, 0, 0],
					[0, 0, 1, 0, 0, 0, 0, 0, 3],
					[3, 0, 0, 0, 0, 0, 0, 0, 2]
	]

	sudoku_s: list = [
					[5, 3, 4, 6, 7, 8, 9, 1, 2],
					[6, 7, 2, 1, 9, 5, 3, 4, 8],
					[1, 9, 8, 3, 4, 2, 5, 6, 7],
					[8, 5, 9, 7, 6, 1, 4, 2, 3],
					[4, 2, 6, 8, 5, 3, 7, 9, 1],
					[7, 1, 3, 9, 2, 4, 8, 5, 6],
					[9, 6, 1, 5, 3, 7, 2, 8, 4],
					[2, 8, 7, 4, 1, 9, 6, 3, 5],
					[3, 4, 5, 2, 8, 6, 1, 7, 9]
					]

	sudoku_test: list = [
						[2, 6, 7, 8, 3, 9, 5, 0, 4],
						[9, 0, 3, 5, 1, 0, 6, 0, 0],
						[0, 5, 1, 6, 0, 0, 8, 3, 9],
						[5, 1, 9, 0, 4, 6, 3, 2, 8],
						[8, 0, 2, 1, 0, 5, 7, 0, 6],
						[6, 7, 4, 3, 2, 0, 0, 0, 5],
						[0, 0, 0, 4, 5, 7, 2, 6, 3],
						[3, 2, 0, 0, 8, 0, 0, 5, 7],
						[7, 4, 5, 0, 0, 3, 9, 0, 1],
	]

	sudoku_test2: list = [
						[6, 4, 9, 2, 8, 3, 1, 5, 7],
						[0, 5, 0, 6, 4, 9, 2, 3, 8],
						[2, 3, 8, 1, 5, 7, 6, 4, 9],
						[9, 2, 3, 8, 1, 5, 0, 6, 4],
						[7, 6, 4, 9, 2, 3, 8, 1, 5],
						[8, 1, 5, 7, 0, 4, 9, 2, 0],
						[5, 7, 6, 4, 9, 2, 3, 2, 1],
						[4, 0, 2, 3, 8, 1, 5, 0, 6],
						[3, 0, 1, 5, 0, 6, 4, 9, 0],
	]
	print(sudoku_grid_correct(sudoku_s))
	print(column_correct(sudoku_test2, 5))
