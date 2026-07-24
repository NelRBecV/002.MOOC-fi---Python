# Write your solution here
def length_of_longest(l_text: list):
	longest = 0
	for w in l_text:
		if len(w) > longest:
			longest = len(w)
	return longest


if __name__=="__main__":
	my_list:list = ["adele", "mark", "dorothy", "tim","rumplestinsky", "hedy", "richard"]
	result = length_of_longest(my_list)
	print(result)
