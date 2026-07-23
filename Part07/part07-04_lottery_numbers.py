from random import shuffle,sample

def lottery_numbers(amount:int,lower:int,upper:int):	    
	    pool = sorted(sample(range(lower,upper),k=amount))   
	    return pool
	    
	 
	if __name__=="__main__":    
	    for lottery in lottery_numbers(7,1,40):
	        print(lottery)
