# Write your solution here
	import difflib


	phrase = input("Write text: ")
	suggestions: dict = {}
	
	with open("wordlist.txt") as words:
	    dictionnary: list = [i.strip() for i in words]
    
	for word in phrase.split(" "):
	    if not word.lower() in dictionnary:
	        phrase = phrase.replace(word,f"*{word}*")
	        suggestions[word] = difflib.get_close_matches(word, dictionnary)
        
	if len(suggestions) !=0:
	    print(phrase)
	    print("suggestions:")
	    for word,s_words in suggestions.items():
	        print(f"{word}: {', '.join(s_words)}")
	 
