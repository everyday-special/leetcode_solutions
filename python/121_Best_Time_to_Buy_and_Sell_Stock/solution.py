class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = prices[0]
        answer = 0
        for i in range(1, len(prices)):
            answer = max(answer, prices[i] - m)
            m = min(prices[i], m)
        return answer
