text = input("Please type in a string:")
	length = len(text)
	if length < 20:
	    sp_left = 20 - length
	    print("*"*sp_left + text)
    
