gift_val=int(input("Value of gift:"))
tax=0
if 5000 <= gift_val < 25000:
	tax = (100+(gift_val-5000)*0.08)
elif 25000 <= gift_val < 55000:
	tax = (1700+(gift_val-25000)*0.10)
elif 55000 <= gift_val < 200000:
	tax = (4700+(gift_val-55000)*0.12)
elif 200000 <= gift_val < 1000000:
	tax = (22100+(gift_val-200000)*0.15)
elif gift_val > 1000000:
	tax = (142100+(gift_val-1000000)*0.17)
else:
	print("No tax!")
if tax != 0:
	print(f"Amount of tax: {tax} euros")
    
