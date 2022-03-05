class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        maxp1 = max(nums) + 1
        points = {}
        for num in nums:
            curr_val = points.get(num, 0)
            points[num] = curr_val + num
        l = [0] * (maxp1)
        if 1 in points:
            l[1] = points[1]
        for i in range(2, maxp1):
            p = points.get(i, 0)
            l[i] = max(l[i-1], l[i-2] + p)
        return l[-1]
