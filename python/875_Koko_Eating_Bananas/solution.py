class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo < hi:
            k = (hi + lo) // 2
            hours = sum([ceil(pile / k) for pile in piles])
            if hours > h:
                lo = k + 1
            else:
                hi = k
        return lo
