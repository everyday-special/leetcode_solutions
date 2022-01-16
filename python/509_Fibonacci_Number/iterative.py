class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n
        curr, prev = 1, 0
        for i in range(n-1):
            curr, prev = curr + prev, curr
        return curr
