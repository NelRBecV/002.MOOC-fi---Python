# WRITE YOUR SOLUTION HERE:
class Person:
	def __init__(self, name: str, height: int):
		self.name = name
		self.height = height
 
	def __str__(self):
		return self.name
 
class Room:
	def __init__(self):
		self.persons = []
		self.total_height = 0
						
	def add(self, person:Person):
		self.persons.append(person)
		self.total_height += person.height
	
	def is_empty(self):
		return len(self.persons) == 0
 
	def shortest(self):
		shorter = 400
	  	persson = ""

		if len(self.persons) == 0:
			return None        
		for short in self.persons:
			if short.height < shorter:
				shorter = short.height
				persson = short
		return persson
 
	def remove_shortest(self):
		short = self.shortest()        
		if not self.is_empty():                    
			if short in self.persons:
				done = short            
				self.persons.remove(short)            
				return done
		return None
 
	def print_contents(self):       
		print(f"There are {len(self.persons)} in the room, and their combined height is {self.total_height} cm")
		for person in self.persons:
			print(f"{person.name} ({person.height})")
		
 
if __name__ == "__main__":
 
	room = Room()
 
	room.add(Person("Lea", 183))
	room.add(Person("Kenya", 172))
	room.add(Person("Nina", 162))
	room.add(Person("Ally", 166))
	room.print_contents()
 
	print()
 
	removed = room.remove_shortest()
	if removed:
		print(f"Removed from room: {removed.name}")
 
	print()
 
	room.print_contents()
 



