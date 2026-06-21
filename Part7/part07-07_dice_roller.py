# Write your solution here
from random import choice


def roll(dice:str):
    '''randomly picks a dice up from a set of dices'''
    
    dice_set = {'A':[3,3,3,3,3,6],'B':[2,2,2,5,5,5],'C':[1,4,4,4,4,4]}
  
    return choice(dice_set[dice])
 
def play(die1:str,die2:str,times:int):
    '''Starts a new dice game and returns the final result of the game'''
  
    game = {'d1_win':0,'d2_win':0,'tie':0}
  
    for throw in range(times):
        throw1 = roll(die1)
        throw2 = roll(die2)
      
        if throw1 > throw2:# first throw wins
            game['d1_win'] +=1
        elif throw1 < throw2:# second throw wins
            game['d2_win'] +=1
        else:
            game['tie'] +=1
    
    return game['d1_win'], game['d2_win'], game['tie']
    
if __name__=="__main__":
    match = play("B","A",100)
    print(match)
    game = play("A","C",200)
    print(game)
