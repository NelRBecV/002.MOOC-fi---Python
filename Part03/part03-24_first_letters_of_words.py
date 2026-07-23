text = input("Please type in a sentence:")
length = len(text)
count = 0
while True:
	index = text.find(" ")
	if index != -1:
		print(text[0])
		text=text[index+1:]
	else:
		print(text[0])
		break
