# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
	"""Returns total of occurrences of each word upper the given limit into a provided text file."""

	with open(filename, "r") as word:
		w = str(word.read()).replace(",", "").replace(".", "")
		words = w.split()
	word_dict = {word: words.count(word) for word in words if words.count(word) >= lower_limit}
	return word_dict


if __name__ == "__main__":
	print(most_common_words("comprehensions.txt", 3))

