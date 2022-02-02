class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        return [wealth := max(wealth, sum(acc)) for acc in accounts][-1]
