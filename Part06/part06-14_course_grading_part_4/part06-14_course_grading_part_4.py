  file_st_path = input("Students information: ")
	file_ex_path = input("Exercises completed: ")
	file_ep_path = input("Exam points: ")
	file_co_path = input("Course information: ")
	 
	#Retrieving students information from selected "students" file
  students:dict = {}
	with open(file_st_path) as data:
	    for st in data:
	        record = st.split(";")
	        if record[0] == "id":
	            continue
	        students.update({record[0]:f"{record[1].strip()} {record[2].strip()}"})

  #Retrieving percentage of excercises completed from selected "excercises" file
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

  #Retrieving exam points from selected "exam_points" file
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

  #Retrieving data from selected "course" file
	course:str=""
	with open(file_co_path) as data:
	    header:list = []
	    for i in data:
	        record = i.split(":")
	        header.append(record[1])
	    course = f"{header[0].strip()}, {int(header[1])} credits"

  #Get all grade from each student and calculate his/her final grade
	results_csv:str = ""
	results_txt = f"{course}\n{'='*len(course)}\n"
	results_txt += f"{'name':30}{'exec_nbr':10}{'exec_pts.':10}{'exm_pts.':10}{'tot_pts.':10}{'grade':10}\n"       
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
            
	    results_txt += f"{name:30}{exercises[id][0]:<10}{exercises[id][1]:<10}{exam_points[id]:<10}{exercises[id][1]+exam_points[id]:<10}{final:<10}\n"
	    results_csv +=f"{id};{name};{final}\n"
	
  #Save procesed data into files
	with open("results.txt",'w') as txt:
	    txt.write(results_txt)
	 
	with open("results.csv",'w') as csv:
	    csv.write(results_csv)
	print("Results written to files results.txt and results.csv")



