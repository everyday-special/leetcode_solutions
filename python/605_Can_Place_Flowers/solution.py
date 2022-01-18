class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            return True if (not flowerbed[0] or n == 0) else False
        i, count = 1, 0
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            flowerbed[0], count = 1, count + 1
        while i < len(flowerbed) - 1 and count < n:
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i], count = 1, count + 1
            i += 1
        if flowerbed[-1] == 0 and flowerbed[-2] == 0:
            flowerbed[-1], count = 1, count + 1
        return count >= n
