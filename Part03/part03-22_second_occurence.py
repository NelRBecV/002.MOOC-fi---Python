text = input("Please type in a string:")
	subs = input("Please type in a substring:")
	sub_text = text
	occur = 0
	pos = 0
	while True:    
	    index = sub_text.find(subs)    
	    if index != -1:        
	        occur += 1
	        pos = len(text)-len(sub_text[index:])
	        sub_text = sub_text[index+len(subs):]       
	        if occur == 2:
	            print(f"The second occurrence of the substring is at index {(pos)}.")
	            break
	    else:
	        print("The substring does not occur twice in the string.")
	        break
	 
