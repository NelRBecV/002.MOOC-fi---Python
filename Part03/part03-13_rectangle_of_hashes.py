width = int(input("Width"))
height = int(input("height"))
if width !=0 and height != 0:
	row = 0
	while row < height:
		print("#"*width)
		row += 1
