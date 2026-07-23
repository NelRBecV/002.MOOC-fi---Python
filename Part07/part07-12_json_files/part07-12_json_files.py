# Write your solution here
	import json
	def print_persons(filename:str):	    
	    records: str = ""
    
	    with open(filename,"r") as data:
	        file_read = data.read()
        
	    records = json.loads(file_read)
    
	    for item in records:
	        print(f"{item['name']} {item['age']} years ({', '.join(item['hobbies'])})")
	 
	if __name__=="__main__":
	    print_persons("file1.json")
