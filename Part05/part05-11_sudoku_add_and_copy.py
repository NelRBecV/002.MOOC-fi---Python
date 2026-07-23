# Write your solution here
	def copy_and_add(sudoku:list, row_no:int, column_no:int, number:int):
	    new_sudoku:list = []; 
    
	    for row in range(len(sudoku)):        
	        rows:list = []
	        for col in range(len(sudoku[row])):                      
	            rows.append(sudoku[row][col])        
	        new_sudoku.append(rows)        
	    
      add_number(new_sudoku,row_no,column_no,number)
    
	    return new_sudoku
	 
	def add_number(sudoku:list, row_no:int, column_no:int, number:int):
	    sudoku[row_no][column_no] = number
	 
	def print_sudoku(sudoku:list):	    
      for row in range(len(sudoku)):
	        for col in range(len(sudoku[row])):
	            if sudoku[row][col] != 0:
	                print(f"{sudoku[row][col]}", end=" ")
	            else:
	                print("_", end=" ")
	            if (col+1) % 3 == 0:
	                print(" ", end=" ")
	        
          print()
	        
          if (row+1) % 3 == 0:
	            print()
	 
	 
	if __name__=="__main__":
	    sudoku  = [
	    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 0, 0],
	    [0, 0, 0, 0, 0, 0, 0, 0, 0]
	    ]
	 
	    grid_copy = copy_and_add(sudoku,5,2,2)   
	    print("Original:")
	    print_sudoku(sudoku)
	    print()
	    print("Modified: ")
	    print_sudoku(grid_copy)



