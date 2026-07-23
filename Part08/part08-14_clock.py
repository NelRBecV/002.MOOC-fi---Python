# Write your solution here:
	class Clock:
	    def __init__(self, hours: int, minutes: int, seconds: int):
	        self.hour = hours
	        self.minute = minutes
	        self.second = seconds
	 
	    def __str__(self):
	        return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
	 
	    def tick(self):
	        if self.hour == 23 and self.second == 59 and self.minute == 59:
	            self.start_over("hours", "minutes", "seconds")
	        elif self.second == 59 and self.minute == 59:
	            self.hour += 1
	            self.start_over("minutes", "seconds")
	        elif self.second == 59:
	            self.minute += 1
	            self.start_over("seconds")
	        else:
	            self.second += 1
	 
	    def start_over(self, *params):
	        for param in params:
	            if param == "seconds":
	                self.second = 0
	            elif param == "minutes":
	                self.minute = 0
	            else:
	                self.hour = 0
	 
	    def set(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
	        self.hour = hours
	        self.minute = minutes
	        self.second = seconds
	 
	 
	if __name__ == "__main__":
	    clock = Clock(11, 59, 55)
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.set(20, 35, 59)
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	    clock.tick()
	    print(clock)
	 
	    clock.set(12, 5)
	    print(clock)
	 



