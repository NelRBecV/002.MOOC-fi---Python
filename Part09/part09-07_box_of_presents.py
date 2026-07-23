# WRITE YOUR SOLUTION HERE:
class Present:
	def __init__(self, name,weight) -> None:
		self.name = name
		self.weight = weight
 
	def __str__(self) -> str:
		return f"{self.name} ({self.weight}Kg)"
 
class Box:
	def __init__(self):
		self.weight = 2
		self.presents = 0
 
	def add_present(self,present:Present):
		self.presents += present.weight
	
	def total_weight(self):
		return self.presents
 
if __name__ == "__main__":
	book = Present("ABC Book", 2)
 
	box = Box()
	box.add_present(book)
	print(box.total_weight())
 
	cd = Present("Pink Floyd: Dark Side of the Moon", 1)
	box.add_present(cd)
	print(box.total_weight())



