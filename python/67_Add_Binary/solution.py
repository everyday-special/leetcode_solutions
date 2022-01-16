class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lenA, lenB = -len(a), -len(b)
        i, carry, answer = -1, 0, ''
        while i >= lenA or i >= lenB:
            chA, chB = 0, 0
            if i >= lenA:
                chA = a[i]
            if i >= lenB:
                chB = b[i]
            chAnswer = (int(chA) + int(chB) + carry) % 2
            carry = (int(chA) + int(chB) + carry) // 2
            answer = str(chAnswer) + answer
            i -= 1
        if carry:
            return '1' + answer
        else:
            return answer
