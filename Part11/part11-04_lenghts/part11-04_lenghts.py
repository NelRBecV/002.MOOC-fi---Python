# WRITE YOUR SOLUTION HERE:
def lengths(lists: list):
    return [len(li) for li in lists]


if __name__ == "__main__":
    a_lot_of_lists = [[1, 2, 3, 4, 5], [324, -1, 31, 7], []]
    print(lengths(a_lot_of_lists))
 
