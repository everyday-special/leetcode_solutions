class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1
        curr, prev1, prev2 = 1, 1, 0
        for i in range(n-2):
            curr, prev1, prev2 = curr + prev1 + prev2, curr, prev1
        return curr
