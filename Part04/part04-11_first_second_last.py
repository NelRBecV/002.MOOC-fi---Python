#Note: There are other ways to do this as well, but the idea of the excercise was trying to do it
#by working with strings only, not with lists.

# Write your solution here
	def first_word(string:str):
	    if string != "":
	        space = string.find(" ")
	        if space != -1:
	            return string[0:space]
	    
	def second_word(string:str):
	    if string != "":
	        sp=0
	        while True:
	            space = string.find(" ")
	            if space != -1:
	                sp+=1                                                                             
	                if sp == 2:
	                   return string[:space] 
	                else:
	                    string = string[space+1:]
	            else:              
	                return string              
	 
	def last_word(string:str):
	    if string != "":
	        while True:
	            space = string.find(" ")
	            if space == -1:
	                return string                
	            else:
	                string = string[space+1:]
	        
	    
	# You can test your function by calling it within the following block
	if __name__ == "__main__":
	    sentence = "once upon a time there was a programmer"
	    print(first_word(sentence))
	    print(second_word(sentence))
	    print(last_word(sentence))
