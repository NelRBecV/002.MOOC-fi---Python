# Write your solution here
	def filter_incorrect(lottery: str = "lottery_numbers.csv"):
	    open("correct_numbers.csv","w").close()
	    l_elements:list = []

      #Get lottery numbers from csv file and separate week description from lottery numbers
	    with open(lottery) as lotto:        
	        for line in lotto:
	            l_elements.append(line.split(";"))
	    
      for record in l_elements:
	        header = record[0].split(" ")
	        body = record[1].split(",")
	        try:
	            int(header[1])# reviews if number of week is a number
	        except:
              #omits this line and jumps to the next
	            continue

          #If everything is ok in header, checks for numbers series
	        if len(body) == 7:
	            lotto_num:list=[]
	            try:
	                for b in body:
                      #checks if each nuumber is between 1 and 39 and is not repeated
	                    if int(b) >=1 and int(b) <=39 and int(b) not in lotto_num:
	                        lotto_num.append(int(b))
	                        print(lotto_num)
	                    else:
	                        raise Exception
	            except Exception: #omits this line and jumps to the next one
	                continue
	        else:
	            continue

          #saves the correct ones into a csv file
	        with open("correct_numbers.csv","a") as correct:            
	            correct.write(f'{record[0]};{record[1]}')
	                               
	 
	if __name__=="__main__":
	    filter_incorrect()
	   



