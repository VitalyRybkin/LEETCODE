"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same.
"""

nums = [0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 5]

length = len(nums)
i = 0
while i < length:
    j = i
    while j < length - 1 and nums[i] == nums[j + 1]:
        nums.remove(nums[j + 1])
        length -= 1
        j = i
    i += 1

print(nums, i)