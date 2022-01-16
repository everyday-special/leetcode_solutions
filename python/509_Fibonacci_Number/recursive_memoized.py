class Solution:
    def __init__(self):
        self.hash_map = {}

    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        else:
            if n-1 not in self.hash_map:
                self.hash_map[n-1] = self.fib(n-1)
            if n-2 not in self.hash_map:
                self.hash_map[n-2] = self.fib(n-2)
            return self.hash_map[n-1] + self.hash_map[n-2]
