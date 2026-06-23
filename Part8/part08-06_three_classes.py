# Write your solution here
	class Checklist:
	    def __init__(self,header:str,entries:list):
	        self.header = header
	        self.entries = entries
	 
	class Customer:
	    def __init__(self,id:str,balance:float,discount:int):
	        self.id = id
	        self.balance = balance
	        self.discount = discount
	 
	class Cable:
	    def __init__(self,model:str,length:float,max_speed:int,bidirectional:bool):
	        self.model = model
	        self.length = length
	        self.max_speed = max_speed
	        self.bidirectional = bidirectional
	 
	if __name__=="__main__":
	    customer1 = Customer("12345678",125.45,15)
	    item1 = Cable("Alfa-12X",25.5,150,True)
	    item2 = Cable("Omega-98BD",132.4,500,False)
	    bill = Checklist("Sale001",[customer1,[item1,item2]])
	 
	    print(f"Our customer {customer1.id}, has a bill of {customer1.balance} so that earned a discount of {customer1.discount}%")
	    print(f"The cable {item1.model}, has {item1.max_speed}Gbps of speed with {item1.length}mts length")
	    print(f"Is {item2.model} a bidirectional cable? {'yes' if item2.bidirectional == 1 else 'no'}")
	 
	    print(f"The transaction {bill.header} by customer {bill.entries[0].id} who bought: ")
    
	    for n in bill.entries[1]:
	        print(f"- {n.model} {n.length} {n.max_speed} {n.bidirectional}")
	   

