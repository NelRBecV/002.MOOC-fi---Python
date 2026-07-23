# Write your solution here
from fractions import Fraction

def fractionate(amount:int):
    fract:list=[]
    
    for i in range(amount):
        fract.append(Fraction(1,amount))
      
    return fract
 
if __name__=="__main__":
    for p in fractionate(3):
        print(p)
 
    print()
 
    print(fractionate(5))
