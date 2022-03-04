class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        diffs = [a - b for a, b in zip(A[1:], A[:-1])]
        count = 1
        answer = 0
        for i, diff in enumerate(diffs[1:], start = 1):
            if diffs[i-1] == diff:
                count += 1
                if count >= 2:
                    answer += count - 1
            else:
                count = 1
        return answer
