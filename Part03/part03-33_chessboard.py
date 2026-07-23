# Write your solution here
	def chessboard(squares:int):
	    times = squares*squares
	    count = 0
	    shape = "1"
	    table = ""
	    while count < squares:
	        line=0
	        while line < squares:
	            table += shape
	            if shape == "1":
	                shape = "0"
	            else:
	                shape="1"          
	            line +=1
	        if squares % 2 == 0:
	            if shape == "1":
	                shape = "0"
	            else:
	                shape="1"
	        print(table)
	        table=""
	        count +=1
	# Testing the function
	if __name__ == "__main__":
	    chessboard(6)
    
	 
