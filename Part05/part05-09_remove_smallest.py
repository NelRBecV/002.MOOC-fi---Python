# Write your solution here
def remove_smallest(numbers: list):
	if len(numbers) > 0:
		new_list: list = []
		small: int = min(numbers)

		for n in numbers:
			if n != small:
				new_list.append(n)
		numbers[:] = new_list


if __name__ == "__main__":
	raw_list: list = [1, 2, 3, 5, 6]
	print(raw_list)
	remove_smallest(raw_list)
	print(raw_list)
