class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        start, prev = nums[0], nums[0]
        answer = []
        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                if start == prev:
                    answer.append(f'{start}')
                else:
                    answer.append(f'{start}->{prev}')
                start = nums[i]
            prev = nums[i]
        if start == prev:
            answer.append(f'{start}')
        else:
            answer.append(f'{start}->{prev}')
        return answer
