# Write your solution here
stock: list= []
items = int(input("How many items: "))
for i in range(items):
	stock.append(int(input(f"item {i+1}: ")))

print(stock)
