# Write your solution here
import re


def is_dotw(my_string: str):  # dotw stands for "Days of the Week"
    week = "|".join(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    if re.search(week, my_string):
        return True
    return False


def all_vowels(my_string: str):
    for vowel in my_string:
        if not re.search(vowel, "aeiou"):
            return False
    return True


def time_of_day(my_string: str):
    if re.search("(2[0-3]|[01][0-9]):[0-5][0-9]:[0-5][0-9]", my_string):
        return True
    return False


if __name__ == "__main__":
    print("Time:")
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))
    print(time_of_day("23:54:37"))

