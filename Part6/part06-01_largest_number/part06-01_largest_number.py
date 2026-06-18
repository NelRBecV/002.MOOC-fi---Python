# write your solution here
	def largest(file:str="numbers.txt"):
	    larger:int=0
	    
      with open(file,'r') as data:
	        for number in data: #directly read lines without using readlines() IO function
	            num = int(number.replace("\n",""))
	            if num>=larger:
	                larger=num
                
	        return larger
	 
	if __name__=="__main__":
	    large = largest()
	    print(large)
