	# Write your solution here
	def row_sums(matrix:list):
		"""Returns total sum of each row in a matrix"""
	    for l in range(len(matrix)):
	        sums = sum(matrix[l])
	        matrix[l].append(sums)
	 
	if __name__=="__main__":
	    my_matrix = [[15,18,25,2,14,6],[3,4,9,7,250,46,2],[8,6,2,1,3],[3,5]]
	    row_sums(my_matrix)
	    print(my_matrix)
