# Write your solution here:
	class Stopwatch:
      """Represents how a Stopwatch works."""
    
	    def __init__(self):
	        self.seconds = 0
	        self.minutes = 0
	 
	    def __str__(self):
	        return f"{self.minutes:02}:{self.seconds:02}"
	 
	    def tick(self):          
	        if self.seconds == 59 and self.minutes == 59:
	            self.start_over("seconds")
	            self.start_over("minutes")        
	        elif self.seconds == 59:
	            self.minutes += 1
	            self.start_over("seconds")
	        elif self.seconds < 59:
	            self.seconds += 1
	 
	    def start_over(self,digit):        
	        if digit == "seconds":
	            self.seconds = 0
	        else:
	            self.minutes = 0
	 
	if __name__=="__main__":
	    counter = Stopwatch()
	    for seg in range(3630):
	        print(counter)
	        counter.tick()



