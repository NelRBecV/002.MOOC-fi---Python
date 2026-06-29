def balanced_brackets(my_string: str):
    signs: list = ["[", "]", "(", ")"]

    if len(my_string) == 0:
        return True

    if my_string[0] not in signs:
        return balanced_brackets(my_string[1:])

    if my_string[-1] not in signs:
        return balanced_brackets(my_string[:-1])

    if my_string[0] == signs[0] and my_string[-1] == signs[1] or my_string[0] == signs[2] and my_string[-1] == signs[3]:
        return balanced_brackets(my_string[1: -1])

    return False


if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # # # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)
