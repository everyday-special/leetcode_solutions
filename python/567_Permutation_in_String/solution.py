class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Faster solution using list with length of 26
        """
        lens1 = len(s1)
        s1_counts = [0] * 26
        for ch in s1:
            s1_counts[ord(ch)-97] += 1
        curr = [0] * 26
        for i in range(len(s2)):
            curr[ord(s2[i])-97] += 1
            if i - lens1 >= 0:
                curr[ord(s2[i-lens1])-97] -= 1
            if curr == s1_counts:
                return True
        return False

    def checkInclusion2(self, s1: str, s2: str) -> bool:
        """
        Slower solution using collections.Counter()
        """
        s1counts, lens1 = Counter(s1), len(s1)
        for i in range(len(s2) - lens1 + 1):
            if Counter(s2[i:i+lens1]) == s1counts:
                return True
        return False
