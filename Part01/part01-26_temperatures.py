# Write your solution here
temp_f = int(input("Please type in a temperature (F):"))
celsius = ((temp_f - 32)*5)/9
print(f"{temp_f} degrees Fahrenheit equals {celsius} degrees Celsius")
if celsius < 0:
	print("Brr! It's cold in here!")
