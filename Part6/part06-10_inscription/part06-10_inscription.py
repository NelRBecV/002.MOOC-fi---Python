name = input("Whom should I sign this to : ")
	filename = input("Where shall I save it: ")
	 
	text_content = f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"
	with open(filename,"w") as file:
	    file.write(text_content)
	 
