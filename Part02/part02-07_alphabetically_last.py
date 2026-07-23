word_1 = input("Please type in the 1st word:")
	word_2 = input("Please type in the 2nd word:")
	if word_1 > word_2:
	    print(f"{word_1} comes alphabeticall last.")
	elif word_1 < word_2:
	    print(f"{word_2} comes alphabeticall last.")
	elif word_1 == word_2:
	    print("You gave me the same word twice.")
    
