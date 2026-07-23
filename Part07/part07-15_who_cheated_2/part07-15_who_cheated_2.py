# Write your solution here
	import csv
	from datetime import datetime
	
  def final_points() -> dict:
      """Returns all valid points of each student from a course database"""
    
	    final_report:dict= {}      
	    
	    with open('start_times.csv') as start, open('submissions.csv') as end:
	        start_t: list = [i for i in csv.reader(start, delimiter=";")]
	        end_t: list = [i for i in csv.reader(end, delimiter=";")]
        
	    for name, time_s in start_t:
	        tasks: dict = {name:{'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0}}
	        init_time = datetime.strptime(time_s, "%H:%M")
        
	        for nam,task,points,time_e in end_t:
	            finnish_time = datetime.strptime(time_e,"%H:%M")
	            if not (finnish_time - init_time).total_seconds() > 10800 and nam == name:                
	                if int(points) > tasks[name][task]:
	                    tasks[name][task] = int(points)
                    
	        final_report.update({name: sum(tasks[name].values())})
        
	    return final_report


	if __name__=="__main__":
    
	    grades = final_points()
	    print(grades)
    
