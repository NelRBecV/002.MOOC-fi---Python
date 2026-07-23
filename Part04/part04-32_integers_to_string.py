# Write your solution here
	def formatted(integers:list):
	    string:list = []
	    for i in integers:
	        string.append(f"{i:.2f}")
	    return string
	 
	if __name__=="__main__":
	    numbers:list=[0.123, 1.23, 0.0234]
	    result=formatted(numbers)
	    print(result)

