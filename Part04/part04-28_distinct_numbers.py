def distinct_numbers(num: list):
	dis: list = []
	for n in num:
		if n not in dis:
			dis.append(n)
	dis.sort()
	return dis


if __name__ == "__main__":
	num_list: list = [5, 7, 41, 2, 9, 123, 0, 5, 41, 9, 12]
	print(distinct_numbers(num_list))
