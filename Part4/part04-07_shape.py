# Copy here code of line function from previous exercise and use it in your solution
	def line(times:int,char:str):
	    if char=="":
	        char="*"
	    print(char[0]*times)
	
  def shape(f_size:int,f_shape:str,s_size:int,s_shape:str):
	    for l in range(f_size):
	        line(l+1,f_shape)
	    count=0
	    while True:        
	        if count < s_size:
	            line(f_size,s_shape)
	        else:
	            break
	        count +=1
	 
	# You can test your function by calling it within the following block
	if __name__ == "__main__":
	    shape(3, "i", 6, "j")

