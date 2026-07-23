from datetime import datetime
from string import digits


def is_it_valid(pic: str):
    """
        Returns TRUE if a vehicle plate is valid. This is based on finnish plates format

        The format is as follows:
        characters 1-6: person's birthdate (dd/mm/yy)
        character 7: symbol that indicates the century person was born
        characters 8-10: individual number. Odd for men, even for women
        character 11: control character. It is found by dividing all nine numbers together by 31 searched on a table that goes from 0 to Y excluding some alphabetical characters
    """

    # Finnish plates must be 11 characters. neither less, nor more
    if len(pic) != 11:
        return False

    # Sets control characters (letters and numbers) allowed and stablished separators used in PIC's
    separator = {'+': 1800, '-': 1900, 'A': 2000}
    control_characters = digits + 'ABCDEFHJKLMNPRSTUVWXY'
    sections: list = []    
    cent_year = 0

    for i in pic:
        if not i.isdigit():
            sections = pic.split(i)
            cent_year = separator[i]
            break

    day, month, year = int(sections[0][:2]), int(sections[0][2:4]), int(sections[0][4:6])
    # Transforms two-digits year into four
    year += cent_year
    
    # Checks on a valid date value
    try:
        date = datetime(year=year, month=month, day=day)
    except ValueError:
        return False
        
    all_numbers_together: str = sections[0] + sections[1][:-1]
    
    # Retrieves decimal value and multiply by 31 in order to obtain the integer value
    decimal_number: str = "0." + str((int(all_numbers_together) / 31)).split(".")[1]    
    pic_remainder = round(float(decimal_number) * 31)
    
    # Verifies if the remainder result matches with the control character given
    if sections[1][len(sections[1]) - 1] == control_characters[pic_remainder]:
        return True
    else:
        return False


if __name__ == "__main__":
    val = is_it_valid("050882-437X")
    print(val)
