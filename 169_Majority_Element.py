"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

nums = [2,2,1,1,1,2,2]

def majorityElement(nums: list[int]) -> int:
    maj_dic = {}
    for k,v in enumerate(nums):
        if v not in maj_dic:
            maj_dic[v] = 1
        else:
            maj_dic[v] += 1
        if maj_dic[v] > len(nums) / 2:
            return v


print(majorityElement(nums))