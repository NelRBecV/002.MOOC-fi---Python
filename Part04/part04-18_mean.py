# Write your solution here
def mean(data: list):
	if data != "":
		mean_value = 0
		for n in data:
			mean_value += n
		return mean_value/len(data)


# You can test your function by calling it within the following block
if __name__ == "__main__":
	my_list = [-3, 6, -4]
	result = mean(my_list)
	print(result)
