# Write your solution here
	while True:
	    print("1 - Add word, 2 - Search, 3 - Quit")
	    sel = int(input("Function: "))
	    
      if sel == 3:# ends the program
	        print("Bye!")
	        break
	    
      elif sel == 2:# Searches for an existent word from the available words in dictinary.txt
	        search:list = []
	        fragm = input("Search term: ")
	        with open("dictionary.txt") as dictionary:
	            for word in dictionary:
	                if fragm in word:
	                    fin,eng = word.split(";")
	                    search.append(f"{fin.strip()} - {eng.strip()}")
	        show = [print(s) for s in search]
	    
        elif sel == 1:# adds a new word into dictionary file
	        finnish = input("The word in finnish: ")
	        english = input("The word in english: ")
	        with open("dictionary.txt","a") as new_entry:
	            new_entry.write(f"{finnish};{english}\n")
	        print("Dictionary entry added")
	    else:
	        print("not a valid option!")
