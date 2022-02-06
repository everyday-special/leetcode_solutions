# Naive solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_num, count = nums[0], 0
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] == curr_num:
                count += 1
            else:
                curr_num, count = nums[fast], 1
            if count <= 2:
                if slow != fast:
                    nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
