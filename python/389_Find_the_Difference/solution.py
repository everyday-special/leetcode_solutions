class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        answer = ord(t[-1])
        for i in range(len(s)):
            answer = answer ^ ord(s[i]) ^ ord(t[i])
        return chr(answer)
