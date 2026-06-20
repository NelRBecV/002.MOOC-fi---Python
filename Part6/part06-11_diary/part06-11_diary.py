op:str = ""
	while op != "0":
	    print("1 - add an entry, 2 - read entries, 0 - quit")
	    op = input("Function: ")
	    
      if op == "1":
	        entry = input("Diary entry: ")
	        with open("diary.txt","a") as file:
	            file.write(f"{entry}\n")
	            print("Diary saved")
	    elif op == "2":
	        with open("diary.txt") as data:
	            print("Entries: ")
	            for entry in data:
	                print(entry.strip())
	    else:
	        print("Bye now!")
	         
