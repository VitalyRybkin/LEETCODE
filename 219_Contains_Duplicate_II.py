"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.
"""
# nums = [1,2,3,1] # t
# k = 3
# nums = [1,0,1,1] # t
# k = 1
nums = [1,2,3,1,2,3] # f
k = 2
# nums = [4,1,2,3,1,5] # t
# k = 3
# nums = [99,99]
# k = 2

import time

def containsNearbyDuplicate(nums: list[int], k: int) -> bool:

        count_dict = {}
        for key, val in enumerate(nums):
            if not val in count_dict.keys():
                count_dict[val] = key
            else:
                if abs(count_dict[val] - key) <= k:
                    return True
                else:
                    count_dict[val] = key

        return False


st = time.time()
print(containsNearbyDuplicate(nums, k))
et = time.time()
print(et - st)
