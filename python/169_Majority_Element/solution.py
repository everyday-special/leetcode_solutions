# Naive solution using collections.Counter()

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts, key=counts.get)

# Linear time, constant space solution after reading discussion

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority, freq = nums[0], 0
        for num in nums:
            if num == majority:
                freq += 1
            else:
                freq -= 1
                if freq == 0:
                    majority, freq = num, 1
        return majority
