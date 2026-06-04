def mean(*data):
	    length=len(data)
	    count=0
	    total=0
	    while count<length:
	        total += data[count]
	        count +=1
	    print(total/len(data))
	# Testing the function
	if __name__ == "__main__":
	    mean(10, 1, 1)
    
