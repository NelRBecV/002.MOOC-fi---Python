# Write your solution here
def most_common_character(text: str):
	most_repeated_letter: str = ""
	count = 0
	for t in text:
		rep = text.count(t)
		if rep > count and t != " ":
			most_repeated_letter = t
			count = rep
	return most_repeated_letter


if __name__ == "__main__":
	phrase = "This is the most beautiful thing I ever done"
	repeated_letter = most_common_character(phrase)
	print(repeated_letter)
