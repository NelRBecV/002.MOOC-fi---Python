limit = int(input("Upper limit:"))
base = int(input("Base:"))
power=0
count = 0
while base**count <= limit:
	power = base**count
	print(power)
	count +=1
