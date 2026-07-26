# WRITE YOUR SOLUTION HERE:
def lengths(string:list):
    return {word: len(word) for word in string}
 
if __name__ == "__main__":
    word_list = ["once", "upon", "a", "time", "in"]
 
    word_lengths = lengths(word_list)
    print(word_lengths)
 
