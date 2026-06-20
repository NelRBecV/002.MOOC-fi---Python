# Write your solution here
	def filter_solutions():
      #Creates files that will be filled with
	    open("correct.csv","w").close()
	    open("incorrect.csv","w").close()

      #Opens the file with the data
	    with open("solutions.csv") as data:
	        for line in data:
	            test = line.split(";")
              
              #performs the operation related to student test
	            result = eval(test[1])
              
              #checks if the result matches with the student answer and save it in its respective file
	            if result == int(test[2]):
	                with open("correct.csv","a") as correct_ans:
	                    correct_ans.write(line)
	            else:
	                with open("incorrect.csv","a") as inc_answers:
	                    inc_answers.write(line)
	 
	if __name__=="__main__":
	    filter_solutions()
	    filter_solutions()
	    filter_solutions()
	    filter_solutions()
	    filter_solutions()
