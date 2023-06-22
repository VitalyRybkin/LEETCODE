"""
Given a string s, find the length of the longest
substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        if s:
            substring = list()
            substring.append(s[0])
            length = 1
            for i in range(1, len(s)):
                if s[i] in substring:
                    if length < len(substring):
                        length = len(substring)
                    get_length = len(substring[:substring.index(s[i]) + 1])
                    substring = substring[get_length:]
                substring.append(s[i])
                if i == len(s) - 1 and length < len(substring):
                    length = len(substring)

        return length


l = Solution()
print(l.lengthOfLongestSubstring('au'))
