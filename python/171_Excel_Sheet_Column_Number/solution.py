class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for ch in columnTitle:
            num = num * 26 + ord(ch) - 64
        return num
