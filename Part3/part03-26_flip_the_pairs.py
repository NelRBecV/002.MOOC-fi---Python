	number=int(input("Please type in a number:"))
	jump = 1
	while True:
	    if jump<number:
	        print(jump+1)
	        print(jump)
	    else:
	        if number % 2 !=0:
	            print(jump)
	        break   
	    jump+=2
    
