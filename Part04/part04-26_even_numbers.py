def even_numbers(numbers:list):
	    even:list = []
	    for n in numbers:
	        if n % 2 == 0:
	            even.append(n)
	    return even
	 
	if __name__=="__main__":
	    o_list = [1,5,2,9,7,4,12]
	    even_list = even_numbers(o_list)
	    print(f"original {o_list}")
	    print(f"new {even_list}")
    
