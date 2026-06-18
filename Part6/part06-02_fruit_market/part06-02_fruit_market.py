# write your solution here
	def read_fruits():
	    market:dict = {}
    
	    with open("fruits.csv","r") as fruits:                
	        for fruit in fruits:
	            price_list = fruit.split(";")        
	            market.update({price_list[0]:float(price_list[1])})           
	    return market
	 
	if __name__=="__main__":
	    price = read_fruits()
	    print(price)
	 
