# Write your solution here
	def read_input(message: str, min: int,max: int):
	    while True:        
	        try:
	            number = int(input(message))
	            if number >= min and number <=max:
	                return number
	            else:
	                raise ValueError
	        except ValueError:
	            print(f"You must type in an integer between {min} and {max}")
	        
	 
	if __name__=="__main__":
	    num = read_input("please type in a number: ", 5,10)
	    print("You typed in:", num)

