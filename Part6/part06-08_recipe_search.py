# Write your solution here
	def search_by_name(filename:str,word:str):
      '''Searches recipes by its name'''
    
	    recipes:dict = {}	    
      with open(filename) as data:
	        splitted_data:list = []	        
          for recipe in data:
              #Adds each line from file on a new list and creates a new entry in dictionary if the value of "recipe" is empty or EOF
	            splitted_data.append(recipe.strip())
	            if recipe.strip() == "":                                                    
	                recipes.update({splitted_data[0]:{"time":int(splitted_data[1]),"ingredients":splitted_data[2:len(splitted_data)-1]}})
	                splitted_data.clear()
	        else:
	            recipes.update({splitted_data[0]:{"time":int(splitted_data[1]),"ingredients":splitted_data[2:len(splitted_data)-1]}})
            
	    name_output:list = []
	    for name in recipes.keys():
	        if word in str(name).lower():
	            name_output.append(name)
            
	    return name_output
	    
	def search_by_time(filename:str,prep_time:int):
      '''Searches recipes by its time of preparation'''

	    recipes:dict = {}
	    with open(filename) as data:
	        splitted_data:list = []
	        
          for recipe in data:
	            splitted_data.append(recipe.strip())
              #Adds each line from file on a new list and creates a new entry in dictionary if the value of "recipe" is empty or EOF
	            if recipe.strip() == "":
	                recipes.update({splitted_data[0]:{"time": int(splitted_data[1]), "ingredients":splitted_data[2:]}})
	                splitted_data.clear()
	        else:
	            recipes.update({splitted_data[0]:{"time": int(splitted_data[1]), "ingredients":splitted_data[2:]}})    
	    
      time_output:list = []
	    for name, recipe in recipes.items():
	        if prep_time >= recipe['time']:
	            time_output.append(f"{name}, preparation time {recipe['time']} min")
	    
      return time_output
	 
	def search_by_ingredient(filename:str, ingredient:str):
      '''Searches recipes that contains the selected ingredient'''

	    recipes:dict = {}
	    with open(filename) as data:
	        splitted_data:list = []
                  
          for recipe in data:
	            splitted_data.append(recipe.strip())
              #Adds each line from file on a new list and creates a new entry in dictionary if the value of "recipe" is empty or EOF
	            if recipe.strip() == "":
	                recipes.update({splitted_data[0]:{"time":int(splitted_data[1]),"ingredients":splitted_data[2:]}})
	                splitted_data.clear()
	        else:
	               recipes.update({splitted_data[0]:{"time":int(splitted_data[1]),"ingredients":splitted_data[2:]}})    
	    
      ingredient_output:list = []
	    for name, items in recipes.items():
	        ingr:str= " ".join(items['ingredients'])
	        if ingredient in ingr:
	            ingredient_output.append(f"{name}, preparation time {items['time']} min")
	    
      return ingredient_output
	 
	if __name__=="__main__":   
	    
	    recipe_path = input("Enter your recipes file: ")
	    
	    recipe_name: str = input("Please enter recipe's name: ")
	    name: list = search_by_name(recipe_path,recipe_name)
	    for n in name:
	        print(n)
	 
	    recipe_time: int = int(input("Please enter recipe's preparation time: "))
	    times: list = search_by_time(recipe_path,recipe_time)
	    for t in times:
	        print(t)
	 
	    recipe_ingr: str = input("Please enter an ingredient from recipe: ")
	    ingr: list = search_by_ingredients(recipe_path,recipe_ingr)
	    for i in ingr:
	        print(i)
	 
