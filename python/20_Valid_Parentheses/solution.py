class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(chr(ord(ch) + 1) if ch == '(' else chr(ord(ch) + 2))
            elif not stack or ch != stack.pop():
                return False
        return not stack
