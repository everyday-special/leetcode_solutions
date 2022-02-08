# From https://en.wikipedia.org/wiki/Digital_root (hint #4)

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9==0:
            return 9
        else:
            return num % 9
