# Write your solution here
	wage = float(input("Hourly wage: "))
	hours = int(input("Hours worked: "))
	day = input("Day of the week: ")
	if day == "Sunday":
	    wage *=2
	daily = wage * hours
	print(f"Daily wages: {daily} euros")
