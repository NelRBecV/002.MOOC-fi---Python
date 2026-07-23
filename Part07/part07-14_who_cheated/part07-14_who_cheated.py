# Write your solution here
	import csv
	from datetime import datetime


	def cheaters():
	    cheater:list = []
            
      with open('start_times.csv') as start_time, open('submissions.csv') as end_time:
	        start_t: list = [i for i in csv.reader(start_time, delimiter=';')]
	        end_t: list = [i for i in csv.reader(end_time, delimiter=";")]
	    
      for start in start_t:          
	        task_s = datetime.strptime(i[1],"%H:%M")
        
	        for end in end_t:              
	            if start[0] == end[0]:                  
	                task_f = datetime.strptime(end[3],"%H:%M")                
                  #If this student took more than 3 hours to finish an excercise, it is considered as he/she cheated on
	                if (task_f - task_s).total_seconds() > 10800 and not start[0] in cheater:                    
	                    cheater.append(i[0])
	                   
	    return cheater
	 
	if __name__ == "__main__":
	    print(cheaters())
    
