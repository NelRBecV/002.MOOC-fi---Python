# Write your solution here
def same_chars(text: str, *index):
	if len(text) > index[0] >= 0 and len(text) > index[1] >= 0:
		return text[index[0]] == text[index[1]]
	else:
		return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
	print(same_chars("penoso", 3, 15))
