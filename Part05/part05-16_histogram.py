# Write your solution here
def histogram(word:str):
	histo: dict = {}

	for letter in word:
		if letter not in histo:
			histo[letter] = 0
		histo[letter] += 1

	for key, value in histo.items():
		print(f"{key}", "*"*value)


if __name__ == "__main__":
	histogram("abba")
