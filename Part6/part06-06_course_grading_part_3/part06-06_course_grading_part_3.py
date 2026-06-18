# tee ratkaisu tänne
	file_st_path = input("Students: ")
	file_ex_path = input("Exercises: ")
	file_ep_path = input("Exam points: ")

  #Get students personal data
	students:dict = {}
	with open(file_st_path) as data:
	    for st in data:
	        record = st.split(";")
	        if record[0] == "id":
	            continue
	        students.update({record[0]:f"{record[1].strip()} {record[2].strip()}"})

  #Get students' exam grades
	exercises:dict={}
	with open(file_ex_path) as data:
	    for exe in data:
	        st_exe:list = exe.split(";")
	        exe_points:int = 0
	        if st_exe[0] == "id":
	            continue        
	        for points in range(1,len(st_exe)):
	            num = int(st_exe[points])
	            exe_points += num
	 
	        exercises.update({st_exe[0]:(exe_points,int(exe_points/4))})

  #Get students' excercises points
	exam_points:dict={}
	with open(file_ep_path) as data:
	    for ep in data:
	        ep_record:list = ep.split(";")
	        if ep_record[0] == "id":
	            continue
	        ep_final:int = 0
	        for ep_grade in range(1,len(ep_record)):
	            ep_final += int(ep_record[ep_grade])
	        exam_points.update({ep_record[0]:ep_final})
        
  #report headers   
	t1 = "name"
  t2 = "exec_nbr"
  t3 = "exec_pts."
  t4 = "exm_pts."
  t5 = "tot_pts."
  t6 = "grade"

  #print headers
	print(f"{t1:30}{t2:<10}{t3:<10}{t4:<10}{t5:<10}{t6:<10}")

  #claculating final grade for each student
  for id, name in students.items():
	    final:int = 0
	    if id in exercises and id in exam_points:
	        tot:int = exam_points[id] + exercises[id][1]
	        if 15 <= tot <= 17:
	            final = 1
	        elif 18 <= tot <= 20:
	            final = 2
	        elif 21 <= tot <= 23:
	            final = 3
	        elif 24 <= tot <= 27:
	            final = 4
	        elif tot >= 28:
	            final = 5
	        else:
	            final = 0
      
      #Print the result            
	    print(f"{name:30}{exercises[id][0]:<10}{exercises[id][1]:<10}{exam_points[id]:<10}{exercises[id][1]+exam_points[id]:<10}{final:<10}")
    
