# Write your solution here
	def new_person(name:str, age:str):
	    words = name.split(" ")
      
      #Checks if name is a valid data
	    if name.isdigit():        
	        raise ValueError(f'{name} is a number, not a name')
	    elif name == "":        
	        raise ValueError('empty string is not allowed')
	    elif len(name) > 40:        
	        raise ValueError(f"name must be lower than 40 characters, your name has {len(name)} characters")
	    elif len(words) < 2:        
	        raise ValueError(f"name must contain at least 2 words, your name has {len(words)} word")

      #tries if age is a string number, otherwise an exception will be raised
      try:       
	        int(age)
	    except:
	        raise ValueError(f"{age} is not a valid number")           

      #If age is indeed a number, checks if age is a real value
      if int(age) < 0:            
	        raise ValueError(f"{age} is negative. Age value must be greater than zero")        
	    elif int(age) > 150:                    
	        raise ValueError(f"age must be lower than 150. You age is {age}")        
	    
      return name,int(age)
	 
	if __name__=="__main__":
	    name = input("Introduce your name: ")
	    age = input("Your age: ")
	    my_data = new_person(name,age)
	    print(my_data)



