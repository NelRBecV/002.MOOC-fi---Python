# Write your solution here
	def factorials(n:int):
	    fact:dict = {};mult:int=0
    
	    for num in range(1,n+1):
	        mult:int = 1
	        for i in range(1,num+1):
	            mult *= i
	        fact[num] = mult        
        
	    return fact
	 
	if __name__=="__main__":    
	    f = factorials(num)
	    print(f[2])
	    print(f[4])
	    print(f[6])
	 
