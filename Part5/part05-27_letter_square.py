# Write your solution here
#The aim of this excercise is creating square that contains letters without using list type variables

from string import ascii_uppercase

layer = int(input("Layers: "))
letters: str = ascii_uppercase[0: layer][::-1]

if layer == 1:
    print(ascii_uppercase[0])
elif 1 <= layer <= 26:  # We assume the user won't input a number lesser than 1 and greater than 26
    head: str = ""
    half: str = ""
    length: int = layer * 2

    for letter in letters:
        head += letter
        tail: str = ""

        for char in range(0, len(head)):
            tail += head[char]
            if "A" in tail:
                tail = tail[:-1]

        fill: int = length - (len(head) * 2)
        middle: str = ""

        for _ in range(fill-1):
            middle += letter

        half += f"{head}{middle}{tail[::-1]}"
        if letter != "A":
            half += "\n"

    inverted_half: str = half[::-1]
    all_square = half + "\n" + inverted_half[length:]

    print(f"{all_square}")
