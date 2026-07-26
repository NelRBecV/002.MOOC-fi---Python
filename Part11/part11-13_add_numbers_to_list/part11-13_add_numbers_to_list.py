# WRITE YOUR SOLUTION HERE:
def add_numbers_to_list(numbers: list):
	"""adds numbers to a given list by incrementing last value by one until list length is multiple of five."""

	while len(numbers) % 5 != 0:
		numbers.append(max(numbers)+1)
		add_numbers_to_list(numbers)


if __name__ == "__main__":
	numbers = [1, 3, 4, 5, 10, 11]
	add_numbers_to_list(numbers)
	print(numbers)
