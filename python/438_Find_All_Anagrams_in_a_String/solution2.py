# Cleaner solution inspired by discussion

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def idx(ch):
            return ord(ch) - 97

        pattern, curr, answer = [0] * 26, [0] * 26, []
        for ch in p:
            pattern[idx(ch)] += 1
        for ch in s[:len(p)-1]:
            curr[idx(ch)] += 1
        for i in range(len(p)-1, len(s)):
            curr[idx(s[i])] += 1
            if curr == pattern:
                answer.append(i-len(p)+ 1)
            curr[idx(s[i - len(p)+1])] -= 1
        return answer
