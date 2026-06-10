# Write your solution here
	def shortest(words:list):
	    short=""    
	    for w in words:
	        if len(w)<len(short) or len(short) == 0:
	            short = w            
	    return short
	 
	if __name__=="__main__":
	    word_list:list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
	    result=shortest(word_list)
	    print(result)
