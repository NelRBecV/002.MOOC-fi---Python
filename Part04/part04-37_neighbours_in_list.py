# Write your solution here
def longest_series_of_neighbours(numbers: list):
	long = 0
	count = 0
	for n in range(0,len(numbers)-1):
		if abs(numbers[n] - numbers[n+1]) == 1:
			count += 1
			if count > long:
				long = count
		else:
			count = 0
	if long > 0:
		long +=1

	return long


if __name__ == "__main__":
	n_list: list = [1, 3, 5, 7, 10, 11, 14, 15, 19, 20, 21, 22, 3, 25, 25]
	result = longest_series_of_neighbours(n_list)
	print(result)
