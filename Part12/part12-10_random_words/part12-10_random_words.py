# Write your solution here:
from random import randint


def word_generator(characters: str, length: int, amount: int):
	"""
		Retrieves randomly made words according to the given specifications

		characters: str - a string pointing out the target characters to use.
		length: int - the size of each words in terms of characters.
		amount: int - the number of words that will be created.
	"""
	for _ in range(amount):
		random_words = "".join([characters[randint(0, len(characters)-1)] for _ in range(length)])
		yield random_words


if __name__ == "__main__":
	wordgen = word_generator("abcdefg", 10, 5)
	for word in wordgen:
		print(word)
