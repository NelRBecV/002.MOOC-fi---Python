string1 = input("Please type in string 1:")
	string2 = input("Please type in string 2:")
	st1_length = len(string1)
	st2_length = len(string2)
	if st1_length > st2_length:
	    print(f"{string1} is longer")
	elif st1_length < st2_length:
	    print(f"{string2} is longer")
	else:
	    print("The strings are equally long")
    
