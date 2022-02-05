class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maps = {0: -1}
        cumulative, max_len = 0, 0
        for i, num in enumerate(nums):
            if num:
                cumulative += 1
            else:
                cumulative -= 1
            if cumulative in maps:
                max_len = max(max_len, i - maps[cumulative])
            else:
                maps[cumulative] = i
        return max_len
