class Solution:
    def addDigits(self, num: int) -> int:
        answer = 0
        while num > 0:
            answer += num % 10
            answer = answer % 10 + answer // 10
            num = num // 10
        return answer

    # Alternate recursive solution
    def addDigitsRecursive(self, num:int) -> int:
        if num < 10:
            return num
        answer = 0
        while num > 0:
            answer += num % 10
            num = num // 10
        return self.addDigitsRecursive(answer)
