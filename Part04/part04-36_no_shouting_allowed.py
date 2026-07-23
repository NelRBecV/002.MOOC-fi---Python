# Write your solution here
	def no_shouting(words:list):
	    lower_words:list = []
	    for w in words:
	        if not w.isupper():
	            lower_words.append(w)
	    return lower_words
	 
	if __name__ == "__main__":
	    word_list = ["ACA","hola","AHI","Mirenlo","esta","herido"]
	    result = no_shouting(word_list)
	    print(result)
    
