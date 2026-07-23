# Write your solution here
	def double_items(numbers:list):
	    double_list:list = []
    
	    for item in numbers:        
	        double = item*2        
	        double_list.append(double)
        
	    return double_list
	 
	if __name__=="__main__":
	    my_list:list = [1,3,5,7,9,11,13]
	    print("old list:", my_list)
	    print("new list:",double_items(my_list))
