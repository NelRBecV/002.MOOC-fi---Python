# Write your solution here
	my_lst:list = []
	od_lst:list = []
	while True:
	    item = int(input("New item: "))    
	    if item != 0:
	        my_lst.append(item)
	        od_lst.append(item)
	        print(f"The list now: {my_lst}")        
	        od_lst.sort()
	        print(f"The list in order: {od_lst}")
	    else:
	        print("Bye!")
	        break
	    
