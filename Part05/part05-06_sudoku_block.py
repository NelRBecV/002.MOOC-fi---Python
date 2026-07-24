# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for n in numbers:
        rep: int = 0
        for r in range(row_no, row_no + 3):
            for c in range(column_no, column_no + 3):
                if sudoku[r][c] == n:
                    rep += 1
                    if rep > 1:
                        return False
    return True


if __name__ == "__main__":
    my_sudoku = [[9, 0, 0, 0, 8, 0, 3, 0, 0],
                 [2, 0, 0, 2, 5, 0, 7, 0, 0],
                 [0, 2, 0, 3, 0, 0, 0, 0, 4],
                 [2, 9, 4, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 7, 3, 0, 5, 6, 0],
                 [7, 0, 5, 0, 6, 0, 4, 0, 7],
                 [0, 0, 7, 8, 0, 3, 9, 0, 0],
                 [0, 0, 1, 0, 0, 0, 0, 0, 3],
                 [3, 0, 0, 0, 0, 0, 0, 0, 2]
                 ]
    print(block_correct(my_sudoku, 3, 6))
    print(block_correct(my_sudoku, 6, 6))
