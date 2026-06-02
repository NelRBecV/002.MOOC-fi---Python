# Write your solution here
	num1 = int(input("Number 1:"))
	num2 = int(input("Number 2:"))
	op = input("Operation:")
	if op == "add":
	    tot = num1 + num2
	    print(f"{num1} + {num2} = {tot}")
	elif op == "subtract":
	    tot = num1 - num2
	    print(f"{num1} - {num2} = {tot}")
	elif op == "multiply":
	    tot = num1 * num2
	    print(f"{num1} * {num2} = {tot}")
