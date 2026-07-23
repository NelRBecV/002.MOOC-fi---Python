string = input("Please type in a string:")
amount = int(input("Please type in an amount:"))
count = 0
while count < amount:
	count +=1
	output = string * count
print(output)
