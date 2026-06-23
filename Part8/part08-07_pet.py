# Write your solution here:
	class Pet:
	    def __init__(self, name:str,species:str, year_of_birth:int):
	        self.name = name
	        self.species = species
	        self.year_of_birth = year_of_birth
	 
	def new_pet(name:str,species:str,year:int):
      """Creates a new object from Pet class."""    
    
	    animal = Pet(name,species,year)    
	    return animal
	 
	if __name__=="__main__":
	    my_pet = new_pet("Sparky","hamster",2018)
	 
	    print(my_pet.name)
	    print(my_pet.year_of_birth)
	    print(f"My pet's name is {my_pet.name}, it is a {my_pet.species} that was born in {my_pet.year_of_birth}")
	 
