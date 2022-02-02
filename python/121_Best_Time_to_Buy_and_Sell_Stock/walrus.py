class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_price = 0, prices[0]
        return [profit := max(profit, price - (min_price := min(min_price, price))) for price in prices][-1]
