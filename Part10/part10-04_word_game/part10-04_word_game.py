# Write your solution here
import random
 
class WordGame():
    """Runs a word game match"""
  
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds
      
    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)
 
    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")
 
            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie
 
        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")
 
class LongestWord(WordGame):
    """Creates a match where the player who writes the longest word wins the game"""
  
    def __init__(self, rounds:int):
        super().__init__(rounds)

    # Overrides its parent method
    def round_winner(self, player1_word:str, player2_word:str):
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player1_word) < len(player2_word):
            return 2
        else:
            pass
 
class MostVowels(WordGame):
    """Creates a match where the player who writes the word that vowels have most, wins the game"""
  
    vowels = 'aeiou'
    def __init__(self,rounds:int):
        super().__init__(rounds)

    # Overrides its parent method
    def round_winner(self, player1_word:str, player2_word:str):
        w1 = 0; w2 = 0
        for i in player1_word:
            w1 += 1 if i in MostVowels.vowels else 0                
        for k in player2_word:
            w2 += 1 if k in MostVowels.vowels else 0                        
        if w1 > w2:
            return 1
        elif w2 > w1:
            return 2
        else:
            pass 
 
class RockPaperScissors(WordGame):
    """Creates a match from the "Paper, Rock, Scissors" popular game."""
    valid_options = ['paper','scissors','rock']
    def __init__(self, rounds:int):
        super().__init__(rounds)

    # Overrides its parent method
    def round_winner(self, player1_word:str,player2_word:int):
        if not player1_word in RockPaperScissors.valid_options and player2_word in RockPaperScissors.valid_options:
            return 2
        elif not player2_word in RockPaperScissors.valid_options and player1_word in RockPaperScissors.valid_options:
            return 1
        elif not player2_word in RockPaperScissors.valid_options and player1_word not in RockPaperScissors.valid_options:
            pass
        else:
            if player1_word != player2_word:
                if player1_word == "paper" and player2_word == "rock" or player1_word == "rock" and player2_word=="scissors" or player1_word=="scissors" and player2_word == "paper":
                    return 1
                else:
                    return 2
                  
 
if __name__ == "__main__":
    p = RockPaperScissors(3)
    p.play()
 



