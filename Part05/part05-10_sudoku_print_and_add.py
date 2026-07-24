# Write your solution here
def add_number(sudoku: list, row_no:int,column_no: int, input_val: int):
	sudoku[row_no][column_no] = input_val


def print_sudoku(sudoku: list):
	for li in range(len(sudoku)):
		for col in range(len(sudoku[li])):
			if sudoku[li][col] != 0:
				print(f"{sudoku[li][col]}", end=" ")
			else:
				print("_", end=" ")

			if (col+1) % 3 == 0:
				print("", end=" ")

		print()

		if (li+1) % 3 == 0:
			print()


if __name__ == "__main__":
	sudoku_s = [
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0, 0]
	]
	add_number(sudoku_s, 1, 8, 9)
	add_number(sudoku_s, 2, 7, 5)
	add_number(sudoku_s, 4, 3, 3)
	add_number(sudoku_s, 3, 0, 9)
	add_number(sudoku_s, 8, 5, 2)
	print_sudoku(sudoku_s)

