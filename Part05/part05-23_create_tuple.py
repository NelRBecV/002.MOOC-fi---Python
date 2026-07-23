# Write your solution here
	def create_tuple(x:int,y:int,z:int):
	    data:list=[x,y,z]
    
	    return min(data),max(data),sum(data)
	 
	if __name__=="__main__":
	    print(create_tuple(5*5,12,8))
