# Write your solution here
from random import shuffle

def words(n:int,beginning:str):	    
    word_search:list = []
    with open("words.txt") as data:
        for i in data:
            if i.startswith(beginning):
                if not i.strip() in word_search:
                    word_search.append(i.strip())        
                  
    shuffle(word_search)
    print(len(word_search))
  
    if len(word_search) <= n:
        raise ValueError("No word was found using these parameters.")
      
    return word_search[:n]
	 
	if __name__=="__main__":
	    word_list = words(200,"azr")
	    for word in word_list:
	        print(word)
	 
