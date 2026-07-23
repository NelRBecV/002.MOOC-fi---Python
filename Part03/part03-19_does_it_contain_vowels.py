text = input("Please type in a string:")
	length = len(text)
	count = 0
	letter_a=0
	letter_e=0
	letter_o=0
	while count < length:
	    if text[count] == "a":
	        letter_a += 1
	    elif text[count] == "e":
	        letter_e += 1
	    elif text[count] == "o":
	        letter_o += 1
	    count +=1
	if letter_a > 0:
	    print("a found")
	else:
	    print("a not found")
	if letter_e > 0:
	    print("e found")
	else:
	    print("e not found")
	if letter_o > 0:
	    print("o found")
	else:
	    print("o not found")

