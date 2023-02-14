"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.
"""
s = "Hello World"
def lengthOfLastWord(s: str) -> int:
    s_list = list(s.split())
    return len(s_list[len(s_list) - 1])

print(lengthOfLastWord(s))