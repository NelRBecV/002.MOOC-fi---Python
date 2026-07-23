text = input("Word:")
frame = "*"*30
if text != "":
	length = len(text)
	spaces = (28 - length)
	if spaces % 2 == 0:
		spaces = int(spaces/2)
		l_spaces = spaces
		r_spaces = spaces
	else:
		spaces = int(spaces/2)
		l_spaces = spaces + 1
		r_spaces = spaces
	print(frame)
	print("*" + " "*l_spaces + text + " "*r_spaces + "*")
	print(frame)
