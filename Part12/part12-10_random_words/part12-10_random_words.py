# Write your solution here:
	def word_generator(characters: str, length: int, amount: int):
	    from random import randint
	    for _ in range(amount):
	        random_words = "".join([characters[randint(0, len(characters)-1)] for _ in range(length)])
	        yield random_words
	 
	if __name__ == "__main__":
	    wordgen = word_generator("abcdefg", 3, 15)
	    for word in wordgen:
	        print(word)
	    
