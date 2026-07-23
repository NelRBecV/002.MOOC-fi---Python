	# Write your solution here
	def squared(text:int,length:int):    
	    i=0
	    j=0
	    while i < length:        
	        line=""
	        while True:
	            if j == len(text):
	                j=0
	            line +=text[j]
	            j+=1
	            if len(line) == length:
	                break            
	        print(line)
	        i+=1
	if __name__=="__main__":
	    squared("aybabtu",5)
    
