some:str = input("Write text: ")
	dictionary:list = []

	with open("wordlist.txt") as word_list:    
	    for word in word_list:
	        dictionary.append(word.strip())
        
	text = some.split(" ")
	for word in text:    
	    if word.lower() not in dictionary:
	       some = some.replace(f"{word}",f"*{word}*")
        
	print(some)
