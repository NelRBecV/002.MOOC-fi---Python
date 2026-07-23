text = input("Please type a word:")
char = input("Please type a chraracter")
index = text.find(char)
if index < len(text):
	if index+3 < len(text):
		print(text[index:index+3])
