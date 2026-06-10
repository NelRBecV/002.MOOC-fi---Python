# Write your solution here
	items = [1,2,3,4,5]
	while True:
	    index = int(input("Index:"))    
	    if index != -1:
	        if 0 <= index < len(items):
	            new_value = int(input("New value:"))
	            items[index] = new_value
	            print(items)
	    else:
	        break
        
