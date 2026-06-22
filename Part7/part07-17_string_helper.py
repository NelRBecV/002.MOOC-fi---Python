# Write your solution here
	from string import ascii_letters, whitespace, digits


	def change_case(ori_string: str) -> str:
	    new_string:str = ""
    
	    for letter in ori_string:
	        if letter != letter.lower():
	            new_string += letter.lower()
	        elif letter != letter.upper():
	            new_string += letter.upper()
	        else:
	            new_string += letter
            
	    return new_string
	 
	def split_in_half(ori_string:str) -> str:
	    half = int(len(ori_string)/2)
    
	    return ori_string[:half], ori_string[half:]
	 
	def remove_special_characters(ori_string: str) -> str:
	    new_string: str = ""
    
	    for letter in ori_string:
	        if letter in whitespace or letter in ascii_letters or letter in digits:
	            new_string += letter
            
	    return new_string
	 
	if __name__=="__main__":
	    phrase = "Oh nooooo!!!!111 Any way..."
	    print(f"case changed: {change_case(phrase)}")
	    half1,half2 = split_in_half(phrase)
	    print(f"string splitted in half:\n half1: {half1}\n half2: {half2}")
	    print(f"string without special chars: {remove_special_characters(phrase)}")
	 
