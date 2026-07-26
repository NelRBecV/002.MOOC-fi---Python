	# Write your solution here
	def even_numbers(beginning: int, maximun: int):
	    counter = beginning + 1 if beginning % 2 != 0 else beginning    
	    while counter <= maximun:
	        yield counter
	        counter +=2 
	    return counter
	 
	if __name__ == "__main__":
	    even = even_numbers(7,25)
	    for e in even:
	        print(e)
