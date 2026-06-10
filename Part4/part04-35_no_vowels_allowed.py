def no_vowels(text:str):
	    vowels = ['a','e','i','o','u']
	    string=text
	    for v in vowels:
	        exist=text.count(v)
	        if exist != 0:
	            string = string.replace(v,"")
	    return string
	 
	if __name__=="__main__":
	    my_string_chain = "this is an example"
	    result = no_vowels(my_string_chain)
	    print(result)
