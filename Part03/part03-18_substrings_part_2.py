text = input("Please type in a string:")
length = len(text)
count = length-1
while count >=0:
	print(text[count:length])
	count -=1
