# Algorithm from discussion

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        def remove_one_digit(in_nums):
            to_remove = len(in_nums) - 1
            i = 0
            while i < to_remove:
                if ord(in_nums[i]) > ord(in_nums[i+1]):
                    to_remove = i
                else:
                    i += 1
            out_nums = in_nums[:i] + in_nums[i+1:]
            while len(out_nums) > 1 and out_nums[0] == '0':
                out_nums = out_nums[1:]
            if out_nums == '':
                return '0'
            return out_nums
        
        out = num
        for _ in range(k):
            out = remove_one_digit(out)
        return out
