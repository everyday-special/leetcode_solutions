class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequence = '123456789'
        answer = []
        for num_digits in range(2, 10):
            for i in range(len(sequence) - num_digits + 1):
                curr = int(sequence[i:i+num_digits])
                if curr >= low and curr <= high:
                    answer.append(curr)
        return answer
