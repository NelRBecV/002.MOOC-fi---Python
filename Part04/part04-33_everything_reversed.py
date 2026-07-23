def everything_reversed(words:list):
	    rever:list = []
	    for w in words:
	        rever.append(w[::-1])
	    rever.reverse()    
	    return rever
	 
	if __name__=="__main__":
	    my_list = ["This","is","my","programming","in","Python"]
	    result = everything_reversed(my_list)
	    print(result)

