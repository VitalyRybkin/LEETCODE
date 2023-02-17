"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

nums = [1,2,3,4]

def containsDuplicate(nums: list[int]) -> bool:
    return not len(set(nums)) == len(nums)

print(containsDuplicate(nums))