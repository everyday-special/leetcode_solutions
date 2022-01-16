class Solution:
    def myAtoi(self, s: str) -> int:
        answer, i, sign = 0, 0, 1
        s = s.lstrip()
        if not s:
            return 0
        if s[0] in '+-':
            if s[0] == '-':
                sign = -1
            i += 1
        while i < len(s):
            ch = s[i]
            if not ch.isdigit():
                return sign * answer
            answer = 10 * answer + int(s[i])
            i += 1
            if sign * answer > 2 ** 31 - 1:
                return 2 ** 31 - 1
            elif sign * answer < -(2 ** 31):
                return -(2 ** 31)
        answer *= sign
        return answer
