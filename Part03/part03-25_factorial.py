while True:
	number = int(input("Please type in a number:"))
	count = 1
	fact=1
	if number > 0:
		while count <= number:
			fact *= count
			count +=1
	else:
		print("Thanks and bye!")
		break
	print(f"The factorial of the number {number} is {fact}")
