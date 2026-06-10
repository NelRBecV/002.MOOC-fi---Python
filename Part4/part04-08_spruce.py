# Write your solution here
	def spruce(length:int):
	    print("a spruce!")
	    for l in range(length):
	        space = length-1
	        print(f'{(space-l)*" "}{"*"*(l+1)}{"*"*(l)}')
	        if l == length-1:
	            print(space*" "+"*")
	            
	        
	    
	# You can test your function by calling it within the following block
	if __name__ == "__main__":
	    spruce(10)
