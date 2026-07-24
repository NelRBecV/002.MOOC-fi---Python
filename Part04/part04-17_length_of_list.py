# Write your solution here
def length(input_list: list):
	if input_list != "":
		list_length = len(input_list)
		return list_length


# You can test your function by calling it within the following block
if __name__ == "__main__":
	my_list = [3, 6, -4]
	result = length(my_list)
	print(result)

