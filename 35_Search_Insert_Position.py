"""
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

nums = [1,3,5,6]
target = 7

def searchInsert(nums: list[int], target: int) -> int:
    if target < nums[0]:
        return 0
    if target > nums[len(nums) - 1]:
        return len(nums)
    s_idx = 0
    e_idx = (len(nums) - 1)
    while e_idx - s_idx > 1:
        pivot = s_idx + (e_idx - s_idx) // 2
        if target <= nums[pivot]:
            e_idx = pivot
        else:
            s_idx = pivot
        if target == nums[e_idx]:
            return e_idx
        if target == nums[s_idx]:
            return s_idx

    return s_idx if target == nums[s_idx] else s_idx + 1

print(searchInsert(nums, target))
