"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

s = "[([]])"
def isValid(s: str) -> bool:

    parans_dict = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    i = 0
    length = len(s)
    str_list = list(s)
    while i < length:
        if str_list[i] in parans_dict.keys():
            if i - 1 < 0 or not parans_dict[str_list[i]] == str_list[i - 1]:
                return False
            else:
                del str_list[i - 1]
                del str_list[i - 1]
                i -= 1
                length = len(str_list)
        else:
            i += 1

    return len(str_list) < 1

print(isValid(s))