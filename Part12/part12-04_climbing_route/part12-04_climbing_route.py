class ClimbingRoute:
	def __init__(self, name: str, length: int, grade: str) -> None:
		self.name = name
		self.length = length
		self.grade = grade

	def __str__(self) -> str:
		return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution here:


def sort_by_length(routes: list) -> list:
	def get_length(route: ClimbingRoute):
		return route.length
	return sorted(routes, key=get_length, reverse=True)


def sort_by_difficulty(routes: list) -> list:
	def get_difficulty(route: ClimbingRoute):
		return route.grade, route.length
	return sorted(routes, key=get_difficulty, reverse=True)


if __name__ == "__main__":
	r1 = ClimbingRoute("Edge", 38, "6B")
	r2 = ClimbingRoute("Tmooth operator", 11, "6A+")
	r3 = ClimbingRoute("Pynchro", 14, "8A")
	r4 = ClimbingRoute("Small steps", 12, "5C")

	routes = [r1, r2, r3, r4]

	print("Sorting routes by difficulty: ")
	for route in sort_by_difficulty(routes):
		print(route)

	print("\nSorting routes by length: ")
	for route in sort_by_length(routes):
		print(route)
