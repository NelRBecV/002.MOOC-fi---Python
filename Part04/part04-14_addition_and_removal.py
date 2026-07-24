# Write your solution here
my_lst: list = []
count = 0
while True:
	print(f"The list is now {my_lst}")
	op = input("a(d)d (r)emove or e(x)it: ")
	if op == "d":
		count +=1
		my_lst.append(count)
	elif op == "r":
		my_lst.remove(count)
		count -= 1
	elif op == "x":
		print("Bye!")
		break
