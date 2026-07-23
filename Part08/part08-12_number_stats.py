# Write your solution here!
	class  NumberStats:
	    def __init__(self):
	        self.numbers:list = []
	 
	    def add_number(self, number:int):
	        self.numbers.append(number)
	 
	    def count_numbers(self):
	        return len(self.numbers)
	    
	    def get_sum(self):
	        return sum(self.numbers) if self.count_numbers() > 0 else 0
	    
	    def average(self):
	        return round(self.get_sum()/self.count_numbers(),1) if self.count_numbers() > 0 else 0
	 
	 
	num = NumberStats()
	odd = NumberStats()
	eve = NumberStats()	
	 
	while True:
	    n = int(input())
	    if n != -1:
	        if n % 2 == 0:
	            eve.add_number(n)
	        else:
	            odd.add_number(n)
	        num.add_number(n) 
	    else:
	        break
	
	print(f"Sum of numbers: {num.get_sum()}")
	print(f"Mean of numbers: {num.average()}")
	print(f"Sum of even numbers: {eve.get_sum()}")
	print(f"Sum of odd numbers: {odd.get_sum()}")
	
