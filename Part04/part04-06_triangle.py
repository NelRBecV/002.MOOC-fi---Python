# Copy here code of line function from previous exercise
def line(times: int, char: str):
	if char == "":
		char = "*"
	print(char[0]*times)


def triangle(size):
	# You should call function line here with proper parameters
	for l in range(size):
		line(l+1, "#")


# You can test your function by calling it within the following block
if __name__ == "__main__":
	triangle(5)
