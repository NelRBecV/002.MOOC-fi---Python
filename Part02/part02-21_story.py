last_word = ""
	phrase = ""
	while True:
	    word = input("Please type in a word: ")      
	    if word != last_word and word != "end":
	        last_word = word
	        phrase += word + " "  
	    else:
	        print(phrase)
	        break
        
