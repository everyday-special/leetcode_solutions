class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s): i += s[i] == ch
        return i == len(s)
