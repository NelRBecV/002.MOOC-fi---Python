# Write your solution here
	def mean(data:list):
	    if data != "":
	        mean=0
	        for n in data:
	            mean+=n
	        return mean/len(data)
	 
	# You can test your function by calling it within the following block
	if __name__ == "__main__":
	    my_list = [-3, 6, -4]
	    result = mean(my_list)
	    print(result)
