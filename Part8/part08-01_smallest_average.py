# Write your solution here
	def smallest_average(person1:dict,person2:dict,person3:dict):
	    p1: list = [i for i in person1.values()]
      p2: list = [i for i in person2.values()]
      p3: list = [i for i in person3.values()]    
	    smallest:dict = {}

	    if sum(p1[1:]) < sum(p2[1:]) and sum(p1[1:]) < sum(p3[1:]):	        
	        smallest = person1
	    elif sum(p2[1:]) < sum(p1[1:]) and sum(p2[1:]) < sum(p3[1:]):	        
	        smallest = person2
	    elif sum(p3[1:]) < sum(p1[1:]) and sum(p3[1:]) < sum(p2[1:]):	        
	        smallest = person3
	    
	    return smallest
	 
	if __name__=="__main__":
	    person1 = {'name':'pin','result1':4,'result2':1,'result3':0}
	    person2 = {'name':'pan','result1':3,'result2':0,'result3':1}
	    person3 = {'name':'pun','result1':2,'result2':2,'result3':2}
	 
	    print(smallest_average(person1,person2,person3))



