# Write your solution here
	def prime_numbers():
	    count = 2
	    while True:                     
	        for n in range(2, count-1):
	            if count % n == 0:
	                break
	        else:      
	            yield count
	 
	        count += 1
	    
	if __name__ == "__main__":
	    prime = prime_numbers()    
	    print(next(prime))
	    print(next(prime))
	    print(next(prime))
	    print(next(prime))
	    print(next(prime))
	    print(next(prime))
	    print(next(prime))
	    print(next(prime))
	    
