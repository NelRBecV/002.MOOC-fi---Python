# Write your solution here
	def transpose(matrix:list):	  
	    transp:list = []
	    print(transp)
    
	    for li in range(len(matrix)):
	        column:list = []
	        for square in range(len(matrix[li])):
	            column.append(matrix[square][li])
	        transp.append(column)
	    matrix[:] = transp
	 
	if __name__=="__main__":
	    matrix_list:list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	    print(matrix_list)
	    transpose(matrix_list)
	    print(matrix_list)
	 
