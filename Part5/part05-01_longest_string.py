# Write your solution here
	def longest(strings:list):
	    long:list = ["",0]
    
	    for word in strings:
	        if len(word) > long[1]:
	            long[0] = word
	            long[1] = len(word)
            
	    return long[0]
	 
	if __name__=="__main__":
	    string = ["seashell","kraken","water","melon","submarine"]
	    print(longest(string))


