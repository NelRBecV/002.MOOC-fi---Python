# Write your solution here
	def sum_of_positives(numbers:list):
	    add=0
	    for n in numbers:
	        if n >0:
	            add += n
	    return add
	 
	if __name__=="__main__":
	    n_list = [-1,-2,-3,-4,-5]
	    print(f"The result is {sum_of_positives(n_list)}")
    
