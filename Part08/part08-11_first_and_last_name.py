# Write your solution here:
	class Person:
	    def __init__(self,name:str):
	        self.name = name
	    
	    def return_first_name(self):
	        return self.name.split(" ")[0]
	    
	    def return_last_name(self):
	        return self.name.split(" ")[1]
	 
	if __name__=="__main__":
	    person1 = Person("John Doe")
	    person2 = Person("Rosa Meltrozo")
	 
	    print(person1.return_first_name())
	    print(person2.return_last_name())
	 
