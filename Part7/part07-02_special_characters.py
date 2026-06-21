import string 

def separate_characters(my_string: str):    	    
	    alph:str = ""
      punc:str = ""
      special:str = ""

	    for letter in my_string:
	        if letter in string.ascii_letters:
	            alph += letter
	        elif letter in string.punctuation:
	            punc += letter
	        else:
	            special += letter
            
	    return alph, punc, special
	 
	if __name__=="__main__":
	    low_high, punct, special = separate_characters("Olé!!! Hey, are ümläüts wörking?")
	    print(low_high)
	    print(punct)
	    print(special)
