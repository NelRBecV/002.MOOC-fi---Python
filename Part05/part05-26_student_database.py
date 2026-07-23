# Write your solution here
	def add_student(database:dict,name:str):
	    courses:list = []
    
	    if not name in database:
	        database[name] = ""    
	    database[name] = courses
	 
	def add_course(database:dict,name:str,courses:tuple):     
	    if name in database and courses[1] > 0:
	         database[name].append(courses)       
        
	    for course in database[name]:
	        for same_course in database[name]:
	            if course[0] in same_course[0]:
	                if course[1] > same_course[1]:
	                    database[name].remove(same_course)
	 
	def print_student(database:dict, name:str):
	    grades:int = 0; 
    
	    if name in database and database[name] != "":
	        print(f"{name}: ")        
	        if len(database[name]) == 0:
	            print(" no completed courses")
	        else:           
	            print(f" {len(database[name])} completed courses:")
	            for course in database[name]:
	                print(f"  {course[0]} {course[1]}")
	                grades += course[1]
	            print(f" average grade {grades/len(database[name]):.1f}")
	    else:
	        print(f"{name}: no such person in the database")
	 
	def summary(database:dict):    
	    print(f"students {len(database)}")
	    course_count:tuple = ("",0)
	    greater_average:tuple = ("",0)
    
	    for student in database:
	        grade:int=0
	        for g in database[student]:
	            grade +=g[1]
            
	        final_grade = grade/len(database[student])
        
	        if final_grade > greater_average[1]:
	            greater_average = student,final_grade
	        if 0 < len(database[student]) > course_count[1]:         
	            course_count = student,len(database[student]) 
            
	    print(f"most courses completed {course_count[1]} {course_count[0]}")
	    print(f"best average grade {greater_average[1]:.1f} {greater_average[0]}")
    
	            
	if __name__=="__main__":    
	    students = {}
	    add_student(students, "Emily")
	    add_student(students, "Peter")
	    add_course(students, "Emily", ("Software Development Methods", 4))
	    add_course(students, "Emily", ("Software Development Methods", 5))
	    add_course(students, "Peter", ("Data Structures and Algorithms", 3))
	    add_course(students, "Peter", ("Models of Computation", 0))
	    add_course(students, "Peter", ("Data Structures and Algorithms", 2))
	    add_course(students, "Peter", ("Introduction to Computer Science", 1))
	    add_course(students, "Peter", ("Software Engineering", 3))   
	    print_student(students, "Peter")
	    print_student(students, "Emily")
	    print_student(students, "Jack")    
	    summary(students)



