"""
My original thought was to do a 2 pointer solution
but the possibility of negative numbers in nums
made that not a viable solution. I checked the
discussion and was guided in writing this solution.
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        answer, currSum, dic = 0, 0, defaultdict(int)
        for num in nums:
            currSum += num
            answer += (currSum == k)
            answer += dic[currSum - k]
            dic[currSum] += 1
        return answer
