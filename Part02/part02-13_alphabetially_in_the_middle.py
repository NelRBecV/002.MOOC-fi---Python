letter_1 = input("1st letter:")
	letter_2 = input("2nd letter:")
	letter_3 = input("3rd letter:")
	middle=""
	if letter_1 < letter_2 and letter_1 < letter_3:    
	    if letter_2 < letter_3:
	        middle = letter_2
	    else:
	        middle = letter_3
	elif letter_2 < letter_1 and letter_2 < letter_3:
	    if letter_1 < letter_3:
	        middle = letter_1
	    else:
	        middle = letter_3
	elif letter_3 < letter_1 and letter_3 < letter_2:
	    if letter_1 > letter_2:
	        middle = letter_2
	    else:
	        middle = letter_1
	print(f"The letter in the middle is {middle}")
