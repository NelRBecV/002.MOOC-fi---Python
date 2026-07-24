# Write your solution here
def greatest_number(*value):
	greater = 0
	for i in value:
		if i > greater:
			greater = i
	return greater


# You can test your function by calling it within the following block
if __name__ == "__main__":
	greatest = greatest_number(15, 24, -88)
	print(greatest)
