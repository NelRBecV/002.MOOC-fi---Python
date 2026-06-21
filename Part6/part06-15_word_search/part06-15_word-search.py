# Write your solution here}
	def find_words(search_term:str):
	    words_found:list = []
	    word_list:list = []
	    term_to_search: str = search_term.lower()

      #Retrieve dictionary from a text file
	    with open("words.txt") as words:
	        for word in words:
	            word_list.append(word.strip())

      #Find a word into the dictionary that is the same as "search_term"
	    length = len(term_to_search)
	    if "." in term_to_search:
	        letters:int = len(term_to_search.replace(".",""))
	        for w in word_list:
	            letter = 0
	            if len(w) == length:                
	                for l in range(len(term_to_search)):
	                    if w[l] == term_to_search[l]:
	                        letter += 1
	                if letter == letters:
	                    words_found.append(w)
      
      #Find a word that matches with the given word segment
	    elif "*" in term_to_search:          
	        term = term_to_search.replace("*","")
	        if term_to_search.endswith("*"):
              #Find a word that starts with the word segment
	            for w in word_list:
	                if w.startswith(term):
	                    words_found.append(w)
	        else:
              #Find a word that ends with the inputted word
	            for w in word_list:
	                if w.endswith(term):
	                    words_found.append(w)
	    else:
	        for w in word_list:
	            if w == term_to_search:
	                words_found.append(w)
                
	    return words_found
	 
	 
	if __name__=="__main__":
	    print(find_words("res*"))



