# Write your solution here
from random import sample
from string import ascii_lowercase

def generate_password(amount:int):	    
    password = sample(ascii_lowercase,k=amount)    
    return "".join(password)
 
if __name__=="__main__":
    for i in range(8):
        print(generate_password(9))
