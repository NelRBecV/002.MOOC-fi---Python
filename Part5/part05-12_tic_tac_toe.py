# Write your solution here
	def play_turn(game_board:list,coord_x:int, coord_y:int, symbol:str):    
	    if 0 <= coord_x <= 2 and 0 <= coord_y <= 2:
	        if game_board[coord_y][coord_x] != "":       
	            return False
	        else:
	            game_board[coord_y][coord_x]=symbol
	            return True
	    else:
	        return False
	 
	if __name__=="__main__":
	    # game_board:list=[["","X",""],["","",""],["","O",""]]
	    game_board = [['O', '', 'O'], ['', '', ''], ['X', '', 'O']]
	    print(play_turn(game_board,3,0,"X"))
	    print(game_board)
	    # print(play_turn(game_board,0,1,"X"))
	    # print(game_board)
	    # print(play_turn(game_board,2,1,"O"))
	    # print(game_board)
	 
