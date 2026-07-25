# write your solution here
def matrix_sum():
	sum_by_row = row_sums()
	return sum(sum_by_row)


def matrix_max():
	max_num: int = 0
	with open("matrix.txt") as data:
		for row in data:
			row_elements = row.split(",")
			for ele in row_elements:
				if int(ele) > max_num:
					max_num = int(ele)
	return max_num


def row_sums():
	sum_num: list = []
	with open("matrix.txt") as data:
		for row in data:
			single_row = row.split(",")
			addition: int = 0
			for n in single_row:
				addition += int(n)
			sum_num.append(addition)

	return sum_num


def matrix():
	print(f"The total sum of file data is: {matrix_sum()}")
	print(f"The maximun found value in the matrix is: {matrix_max()}")


if __name__ == "__main__":
	matrix()
