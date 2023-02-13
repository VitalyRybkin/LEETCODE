"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.
"""

x = 121

def isPalindrome(x: int) -> bool:
    check = x
    res = 0
    while check > 0:
        res = res * 10 + check % 10
        check = check // 10
    return res == x

print(isPalindrome(x))