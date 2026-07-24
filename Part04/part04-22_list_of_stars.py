# Write your solution here
def list_of_stars(lines: list):
	for li in lines:
		print("*"*li)


if __name__ == "__main__":
	list_elements: list = [1, 5, 8, 6, 1, 5, 3, 2, 4]
	list_of_stars(list_elements)
