def list_sum(num: list, den: list):
	items_sum: list = []
	for n in range(len(num)):
		items_sum.append(num[n]+den[n])
	return items_sum


if __name__ == "__main__":
	a: list = [1, 2, 3]
	b: list = [4, 8, 12]
	print(list_sum(a, b))
