class Car:
	def __init__(self):
		self.__fuel_tank = 0
		self.__odometer = 0
 
	def __str__(self) -> str:
		return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__fuel_tank} litres"
 
	def fill_up(self):
		self.__fuel_tank = 60
 
	def drive(self, km:int):        
		if self.__fuel_tank >= km:
			self.__fuel_tank -= km
			self.__odometer += km
 
if __name__=="__main__":
	chavito_hp = Car()
	chavito_hp.fill_up()
	print(chavito_hp)
	chavito_hp.drive(10)    
	
	chavito_hp.drive(20)
	
	chavito_hp.drive(10)
	
	chavito_hp.drive(20)
	print(chavito_hp)
	# chavito_hp.fill_up()
	# print(chavito_hp)
	# chavito_hp.drive(25)
	print(chavito_hp)
 



