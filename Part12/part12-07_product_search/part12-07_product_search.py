# Write your solution here
def search(products: list, criterion: callable):
	result = []
	for product in products:
		if criterion(product):
			result.append(product)
	return result


def cheapest_price(products: list):
	def price(product: tuple):
		return product[1]
	return sorted(products, key=price)


def most_stock(products:list):
	return max(products, key=lambda product: product[1])


if __name__ == "__main__":
	product_list = [("banana", 5.95, 12),
					("apple", 3.95, 3),
					("orange", 4.50, 2),
					("watermelon", 4.95, 22),
					("kale", 0.99, 1)]

	print("Searching products whose quantity is divisible by 4:")
	print(search(product_list, lambda on_stock: on_stock[2] % 4 == 0))

	print("\nRetrieving the product with more units on stock:")
	print(most_stock(product_list))

	print("\nSorting products from the cheapest to the most expensive on stock:")
	for product in cheapest_price(product_list):
		print(product)
