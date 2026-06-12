# Write your solution here
	phone_book:dict = {}
	option:int = 0
	
  while option !=3:
	    option = int(input("command (1 search, 2 add, 3 quit): "))	    
      if option == 1:
	        search_name:str = input("name: ")
	        if search_name in phone_book:
	            print(phone_book[search_name])
	        else:
	            print("no number")
	    elif option == 2:
	        name:str = input("name: ")
	        number:str = input("number: ")
	        if not name in phone_book:
	            phone_book[name] = ""
	        phone_book[name] = number
	        print("ok!")
	    else:
	        print("quitting...")
	 
