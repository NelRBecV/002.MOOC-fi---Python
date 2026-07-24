# Write your solution here
def oldest_person(people: list):
	older: int = 2025
	name: str = ""

	for person in people:
		if older > person[1]:
			older = person[1]
			name = person[0]
		elif older == person[1]:
			name += f"\n{person[0]}"

	return name


if __name__=="__main__":
	person1 = ("Aladin", 1995)
	person2 = ("Richard", 1999)
	person3 = ("Karl", 1995)
	person4 = ("Jason", 1996)
	data = [person1,person2,person3,person4]
	print(oldest_person(data))
