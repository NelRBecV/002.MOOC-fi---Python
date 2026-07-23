# Write your solution here
from random import sample, shuffle
from string import ascii_lowercase, digits    

def generate_strong_password(amount:int,numbers:bool,special:bool):	    
    password:list = []; punct = ['!','?','=','+','-','(',')','#']
  
    if amount >= 4:
        #Sets the range if numbers and symbols if were selected
        extra_characters: int = (amount//2)-1)
        if numbers == True:            
            password.extend(sample(digits,k=(extra_characters))
        if special == True:
            password.extend(sample(punct,k=(extra_characters)))
        
        #Fills the remaining space with alphabetical characters
        password.extend(sample(ascii_lowercase,k=(amount - len(password))))
      
    elif amount == 3:
        #creates a three characters password with a character of each type
        password.extend(sample(ascii_lowercase,k=1))
        password.extend(sample(digits,k=1))
        password.extend(sample(punct,k=1))
    
    else:
        # creates a two characters password with one digit and punctuation mark
        password.extend(sample(digits,k=1))
        password.extend(sample(punct,k=1))    
    
    shuffle(password)
  
    return "".join(password)
 
if __name__=="__main__":
    for i in range(10):        
        print(generate_strong_password(10,False,False))
        
