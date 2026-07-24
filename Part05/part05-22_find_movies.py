# Write your solution here
def find_movies(database:list,search_term:str):
	search_result:list = []

	for movie in database:
		if search_term.lower() in movie['name'].lower():
			search_result.append(movie)

	return search_result


if __name__ == "__main__":
	database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
	{"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
	{"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101},
	{'name': 'Matrix', 'director': "Wackowsky's brothers", 'year': 2001, 'runtime': 111},
	{'name': 'The Terminator', 'director': 'James Cameron', 'year': 1981, 'runtime': 98}
	]

	my_movies = find_movies(database, "AT")
	print(my_movies)

