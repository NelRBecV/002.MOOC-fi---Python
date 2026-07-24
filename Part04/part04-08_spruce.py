# Write your solution here
def spruce(length: int):
	print("a spruce!")
	for li in range(length):
		space = length-1
		print(f'{(space-li)*" "}{"*"*(li+1)}{"*"*li}')
		if li == length-1:
			print(space*" "+"*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
	spruce(10)
