"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

nums = [4,1,2,4,1,2,3]

def singleNumber(nums: list[int]) -> int:
    length = len(nums)
    i = 0
    while i < length:
        if nums[i] in nums[i + 1:]:
            pair = nums[i]
            nums.remove(pair)
            nums.remove(pair)
            length -= 2
        else:
            return nums[i]
        print(nums)

print(singleNumber(nums))