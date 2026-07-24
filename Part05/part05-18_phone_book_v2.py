# Write your solution here
phone_book:dict = {}
option:int = 0
	
while option != 3:
	option = int(input("command (1 search, 2 add, 3 quit): "))
	if option == 1:
		name: str = input("name: ")

		if name in phone_book:
			for i in phone_book[name]:
				print(i)
		else:
			print("no number")

	elif option == 2:
		name: str = input("name: ")
		number: str = input("number: ")

		if name not in phone_book:
			phone_book[name] = []

		phone_book[name].append(number)
		print("ok!")
	else:
		print("quitting...")
