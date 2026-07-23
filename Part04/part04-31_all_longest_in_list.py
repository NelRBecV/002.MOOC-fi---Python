# Write your solution here
	def all_the_longest(words:list):
	    longest:list=[]
	    long = 0
	    for w in words:
	        if len(w) > long:
	            long = len(w)
	            longest.clear()      
	            longest.append(w)
	        elif len(w) == long:
	            longest.append(w)
	    return longest
	 
	if __name__=="__main__":
	    the_list:list = ["adele","reminard", "mark", "dorothy","asthalan", "tim", "hedy","jullieth", "richard"]
	    result = all_the_longest(the_list)
	    print(result)

