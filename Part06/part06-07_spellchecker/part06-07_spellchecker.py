some_text: str = input("Write text: ")
dictionary: list = []

with open("wordlist.txt") as word_list:
    for word in word_list:
        dictionary.append(word.strip())

text = some_text.split(" ")
for word in text:
    if word.lower() not in dictionary:
        some_text = some_text.replace(f"{word}", f"*{word}*")

print(some_text)
