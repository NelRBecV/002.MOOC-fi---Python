# WRITE YOUR SOLUTION HERE:
	class Recording:
	    def __init__(self,length):
	        self.__length:int = 0
	        self.length = length
	    
	    @property
	    def length(self):
	        return self.__length
	 
	    @length.setter
	    def length(self,long):
	        if long < 0:
	            raise ValueError("The length is below to zero")
            
	        self.__length = long
	 
	if __name__ == "__main__":
	    evolution = Recording(-15)
	 
	    print(evolution.length)
	    evolution.length = 25
	    print(evolution.length)
	    # evolution.length = 48
	    # print(evolution.length)
	    
