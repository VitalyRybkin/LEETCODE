"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""


class Solution:
    def reverse(self, x: int) -> int:
        reversed_x = y = 0
        y = abs(x) if x < 0 else x
        while y > 0:
            reversed_x = reversed_x * 10 + y % 10
            y //= 10

        if reversed_x not in range(-2 ** 31, (2 ** 31) - 1):
            return 0

        return reversed_x if x > 0 else reversed_x * (-1)


l = Solution()
print(l.reverse(-120))
