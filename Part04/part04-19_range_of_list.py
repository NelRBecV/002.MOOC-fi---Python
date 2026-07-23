# Write your solution here
	def range_of_list(data:list):
	    if data != "":
	        return max(data)-min(data)
        
	# You can test your function by calling it within the following block
	if __name__ == "__main__":
	    my_list = [-100, 10000, 2012,123,-123,3123,323]
	    result = range_of_list(my_list)
	    print(f"The range of list is {result}")

