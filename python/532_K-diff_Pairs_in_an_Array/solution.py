class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        answer, counts, seen = 0, Counter(nums), set()
        if not k:
            for num in counts:
                if counts[num] >= 2:
                    answer += 1
        else:
            for num in counts:
                if num + k in counts:
                    answer += 1
        return answer
