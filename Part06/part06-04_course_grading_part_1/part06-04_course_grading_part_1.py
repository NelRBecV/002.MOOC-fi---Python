# write your solution here
	student_file:str = input("Student file: ")
	exercise_file:str = input("Exercise file: ")

	#Get students personal data
	students:dict = {}
	with open(student_file) as data:    
	    for student in data:
	        stdt_records = student.split(";")
	        if stdt_records[0] == "id":
	            continue
	        students.update({stdt_records[0]: stdt_records[1].strip() + " " + stdt_records[2].strip()})

	#Get students percentage of excercises completed
	exercises:dict = {}
	with open(exercise_file) as data:    
	    for student in data:
	        xcs_records = student.split(";")
	        if xcs_records[0] == "id":
	            continue
	        grades:list = []
	        for g in range(1,len(xcs_records)):
	            grades.append(int(xcs_records[g]))
	        exercises.update({xcs_records[0]:grades})    

	#Print excercises grade for each student
	for id, name in students.items():    
	    if id in exercises:
	        print(f"{name} {sum(exercises[id])}")
        
