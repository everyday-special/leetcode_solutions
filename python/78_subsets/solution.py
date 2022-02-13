"""
Solution inspired by the discussion.
I was not familiar with bitmasking before today!
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        mask = 2 ** len(nums) - 1
        while mask:
            curr, i, subset = mask, len(nums) - 1, []
            while curr:
                if curr & 1:
                    subset.append(nums[i])
                i, curr = i - 1, curr >> 1
            subsets.append(subset)
            mask -= 1
        return subsets
