# Write your solution here
def anagrams(text: str, compare: str):
	count = 0
	for letter in text:
		if letter in compare:
			count += 1
	if count == len(text) and count == len(compare):
		return True
	return False


if __name__== "__main__":
	print(anagrams("ole","leo"))
	print(anagrams("hola","ola"))

