# Write your solution here
	def count_matching_elements(numbers:list,match:int):
	    count = 0
    
	    for m in range(len(numbers)):
	        for n in numbers[m]:
	            if n == match:
	                count += 1
                
	    return count
	 
	if __name__== "__main__":
	    num = [[5,3,0],[3,9,7],[7,5,8],[4,7,3]]
	    n = 7
	    print(count_matching_elements(numbers=num,match=n))
