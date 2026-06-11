# Write your solution here
	def column_correct(sudoku:list,column_no:int):
	    numbers:list = [1,2,3,4,5,6,7,8,9]   
	    
    for n in numbers:
	        rep:int = 0	        
          for c in range(len(sudoku)):            
	            if sudoku[c][column_no] == n:
	                rep+=1
              elif  sudoku[c][column_no] == 0:
	                blanks += 1    

              if rep > 1 or blanks > 1:
	                    return False
	    
	    return True
	 
	if __name__=="__main__":
	    sud_table:list = [
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
	 
	    print(column_correct(sud_table,8))



