	print("Please type in integer numbers. Type in 0 to finish.")
	count=0
	mean=0
	add=0
	pos=0
	neg=0
	while True:
	    number = int(input("Number:"))
	    if number !=0:
	        count +=1
	        add += number
	        if number <0:
	            neg +=1
	        else:
	            pos +=1
	    else:
	        mean = add/count
	        print(f"Numbers typed in {count}")
	        print(f"The sum of the numbers is {add}")
	        print(f"The mean of the numbers is {mean}")
	        print(f"Positive numbers {pos}")
	        print(f"Negative numbers {neg}")
	        break
        
