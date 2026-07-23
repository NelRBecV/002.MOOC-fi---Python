# Write your solution here
	def store_personal_data(person:tuple):
	    name,age,height = person
	    with open("people.csv","a") as payroll:
	        payroll.write(f"{name};{age};{height}\n")
	 
	if __name__=="__main__":
	    data = [["Marcus Rashford",32,172.9],["Serena Williams",39,183.1],["Atenea Del Castillo",32, 169.6],["Daniel Carvajal",38,171.4]]
	    for d in data:
	        name, age, height = d
	        store_personal_data((name,age,height))
