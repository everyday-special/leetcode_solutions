# Naive solution
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        answers = []
        curr = {}
        pattern = {}
        for ch in p:
            if ch in pattern:
                pattern[ch] += 1
            else:
                pattern[ch] = 1
        for i in range(len(p)):
            if s[i] in curr:
                curr[s[i]] += 1
            else:
                curr[s[i]] = 1
        if curr == pattern:
            answers.append(0)
        for i in range(0, len(s) - len(p)):
            curr[s[i]] -= 1
            if curr[s[i]] == 0:
                curr.pop(s[i])
            if s[i+len(p)] not in curr:
                curr[s[i+len(p)]] = 1
            else:
                curr[s[i+len(p)]] += 1
            if curr == pattern:
                answers.append(i+1)
        return answers

