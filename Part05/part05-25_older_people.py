# Write your solution here
def older_people(people: list, year: int):
	same_year: list = []

	for person in people:
		if person[1] < year:
			same_year.append(person[0])

	return same_year


if __name__ == "__main__":
	person1 = ("Aladin", 1995)
	person2 = ("Richard", 1999)
	person3 = ("Kristen", 1995)
	person4 = ("Jason", 1996)
	person5 = ("Steve", 1985)
	person6 = ("Michael", 1989)
	person7 = ("Lauren", 1995)
	person8 = ("Jason", 1996)
	# data = [person1,person2,person3,person4,person5,person6,person7,person8]
	data = [('Donald', 1982), ('Daisy', 1892), ('Angela', 1965), ('Vladimir', 2000), ('Dunja', 1919), ('Elizabeth', 1921)]
	print(older_people(data, 1995))
