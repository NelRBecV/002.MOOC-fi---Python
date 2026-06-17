# write your solution here
	student_file:str = input("Student file: ")
	exercise_file:str = input("Exercise file: ")
	exam_file:str = input("Exam points: ")
	 
	students:dict = {}
	with open(student_file) as data:    
	    for student in data:
	        record = student.split(";")
	        if record[0] == "id":
	            continue
	        students.update({record[0]: record[1].strip() + " " + record[2].strip()})
	 
	exercises:dict = {}
	with open(exercise_file) as data:    
	    for grades in data:
	        grade = grades.split(";")
	        if grade[0] == "id":
	            continue
	        stdt_grades:int = 0
	        for g in range(1,len(grade)):
	            stdt_grades += int(grade[g])
	        exercises.update({grade[0]:int(stdt_grades/4)})
	 
	exam_points:dict = {}
	with open(exam_file) as data:
	    for exams in data:
	        exam:list = exams.split(";")
	        if exam[0] == "id":
	            continue
	        points:int=0
	        for grade in range(1,len(exam)):
	            points += int(exam[grade])
	        exam_points.update({exam[0]: points})
	 
	for id, name in students.items():
	    if id in exercises and id in exam_points:
	        final_points = exam_points[id] + exercises[id]
	        final_grade = 0
	        if 15 <= final_points <= 17: 
	            final_grade = 1
	        elif 18 <= final_points <= 20:
	            final_grade = 2
	        elif 21 <= final_points <= 23:
	            final_grade = 3
	        elif 24 <= final_points <= 27:
	            final_grade = 4
	        elif final_points >= 28:
	            final_grade = 5
	        else:
	            final_grade = 0
	    print(f"{name} {final_grade}")
	 
