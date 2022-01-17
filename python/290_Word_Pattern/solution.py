class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        seen = set()
        s = s.split()
        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            ch, word = pattern[i], s[i]
            if ch not in hash_map:
                if word not in seen:
                    hash_map[ch] = word
                    seen.add(word)
                else:
                    return False
            elif hash_map[ch] != word:
                return False
        return True
