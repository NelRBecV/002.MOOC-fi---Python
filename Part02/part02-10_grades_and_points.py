points = int(input("How namy points [0-100]:"))
if 100 >= points >= 90:
	print("Grade: 5")
elif 89 >= points >= 80:
	print("Grade: 4")
elif 79 >= points >= 70:
	print("Grade: 3")
elif 69 >= points >= 60:
	print("Grade: 2")
elif 59 >= points >= 50:
	print("Grade: 1")
elif 49 >= points >= 1:
	print("fail")
else:
	print("impossible!")
    
