def palindromes(word:str):
	    revers = ""    
	    revers = word[::-1]
	    if word == revers:
	        print(f"{revers} is a palindrome!")
	        return True        
	    else:
	        print("that wasn't a palindrome")
	        return False
	            
	while True:
	    if palindromes(input("Please type in a palindrome: ")) == True:
	        break
	    
