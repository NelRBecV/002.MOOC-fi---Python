count=0
while True:
	count +=1
	pin = int(input("PIN:"))
	if pin != 4321:
		print("Wrong")
	else:
		if count == 1:
			print("Correct! It only took you one single attempt!")
		else:
			print(f"Correct! It took you {count} attempts")
		break
