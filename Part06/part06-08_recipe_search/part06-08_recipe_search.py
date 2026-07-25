# Write your solution here

def get_recipes_data(filename: str) -> dict:
	"""Returns a database containing information about recipes"""

	recipes: dict = {}
	with open(filename) as data:
		recipes_data: list = data.readlines()

	ind = 0
	while ind < len(recipes_data):
		split_data: list = []
		for recipe in recipes_data[ind:]:
			if not recipe.strip():
				break
			split_data.append(recipe.strip())
		ind += len(split_data) + 1
		# Adds each line from file on a new list and creates a new entry in dictionary if the value of "recipe" is empty or EOF
		recipes.update({split_data[0]: {"time": int(split_data[1]), "ingredients": split_data[2:]}})


	return recipes


def search_by_name(filename: str, word: str):
	"""Searches recipes by its name"""

	recipes: dict = get_recipes_data(filename)
	name_output: list = []
	for name in recipes.keys():
		if word.lower() in str(name).lower():
			name_output.append(recipes[name])
	return name_output


def search_by_time(filename: str, prep_time: int):
	"""Searches recipes by its time of preparation"""

	recipes: dict = get_recipes_data(filename)
	time_output: list = []
	for name, recipe in recipes.items():
		if prep_time >= recipe['time']:
			time_output.append(f"{name}, preparation time {recipe['time']} min")
	return time_output


def search_by_ingredient(filename: str, ingredient: str):
	"""Searches recipes that contains the selected ingredient"""

	recipes: dict = get_recipes_data(filename)
	ingredient_output:list = []
	for name, items in recipes.items():
		ingr: str = " ".join(items['ingredients'])
		if ingredient in ingr:
			ingredient_output.append(f"{name}, preparation time {items['time']} min")

	return ingredient_output


if __name__ == "__main__":
	recipe_path = input("Enter your recipes file: ")

	recipe_name: str = input("Please enter recipe's name: ")
	name: list = search_by_name(recipe_path, recipe_name)
	for n in name:
		print(n)

	recipe_time: int = int(input("Please enter recipe's preparation time: "))
	times: list = search_by_time(recipe_path, recipe_time)
	for t in times:
		print(t)

	recipe_ingr: str = input("Please enter an ingredient from recipe: ")
	ingr: list = search_by_ingredient(recipe_path, recipe_ingr)
	for i in ingr:
		print(i)
