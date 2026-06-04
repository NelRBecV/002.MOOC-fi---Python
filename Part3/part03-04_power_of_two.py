	number = int(input("Upper limit:"))
	power = 0
	count = 0
	while number != 0:
	    power = 2**count
	    if power <= number:
	        print(power)
	        count +=1
	    else:
	        number = 0
        
