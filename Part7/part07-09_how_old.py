	# Write your solution here
from datetime import date

millenium_date = date(year=1999,month=12,day=31)

#checks if the introduced date is valid
try:
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))
    birth_date= date(year=year, month=month, day=day)
    error = False  
except ValueError:
	print(f"ERROR: {day}-{month}-{year} is not a valid date")
	error = True

#if date is correct the program calculates how namy days there is since your born and millenium eve
if not error:
    days_since_millenium = millenium_date - birth_date
    
    if days_since_millenium.days > 0:
        print(f"You were {days_since_millenium.days} days old on the eve of the new millennium.")
    else:
        print("You weren't born yet on the eve of the new millennium.")
 
