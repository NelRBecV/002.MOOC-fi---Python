text = input("Please type in a word:")
	char = input("Please type in a character:")
	length = len(text)
	while True:
	    index = text.find(char)
	    if index != -1:
	        if index+2 < length:
	            print(text[index:index+3])
	            text= text[index+1:]
	            length = len(text)
	        else:
	            break      
	    else:
	        break
        
