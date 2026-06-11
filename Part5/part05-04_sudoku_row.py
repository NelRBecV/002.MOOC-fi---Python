# Write your solution here
	def row_correct(sudoku:list,row_no:int):    
	    numbers:list = [1,2,3,4,5,6,7,8,9]      

	    for n in numbers:
	        rep:int = 0
	        for r in sudoku[row_no]:
	            print(f"{r} == {n}: {r == n}")
	            if r == n:                
	                rep +=1                
              		if rep >= 2:
						return False
                
	    return True
	 
	if __name__=="__main__":
	    sudoku = [
	    [9, 0, 0, 0, 8, 0, 3, 0, 0],
	    [2, 0, 0, 2, 5, 0, 7, 0, 0],
	    [0, 2, 0, 3, 0, 0, 0, 0, 4],
	    [2, 9, 4, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 7, 3, 0, 5, 6, 0],
	    [7, 0, 5, 0, 6, 0, 4, 0, 7],
	    [0, 0, 7, 8, 0, 3, 9, 0, 0],
	    [0, 0, 1, 0, 0, 0, 0, 0, 3],
	    [3, 0, 0, 0, 0, 0, 0, 0, 2]
	    ]
	    print(row_correct(sudoku,5))



