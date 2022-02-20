# Got algorithm from discussion but all code written by me

from sortedcontainers import SortedList

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        nums = SortedList([num * 2 if num % 2 == 1 else num for num in nums])
        result = nums[-1] + 1
        while nums[-1] % 2 == 0:
            if nums[-1] % 2 == 0:
                new = nums.pop() // 2
                nums.add(new)
            result = min(result, nums[-1] - nums[0])
        return result
