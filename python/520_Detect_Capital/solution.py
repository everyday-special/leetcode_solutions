class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppercase, first_upper = 0, (ord(word[0]) >= 65 and ord(word[0]) <= 90)
        for ch in word:
            uppercase += (ord(ch) >= 65 and ord(ch) <= 90)
        if uppercase == len(word) or uppercase == 0 or (uppercase == 1 and first_upper):
            return True
        return False
