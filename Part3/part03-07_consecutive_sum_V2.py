	limit = int(input("Limit:"))
	add=0
	count = 0
	con_sum = ""
	while add < limit:
	    count += 1
	    add += count
	    if count > 1:
	        con_sum += " + "+ str(count)
	    else:
	        con_sum = str(count)
	print(f"The consecutive sum: {con_sum} = {add}")
