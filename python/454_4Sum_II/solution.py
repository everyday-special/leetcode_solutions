class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        nums1and2 = {}
        answer = 0
        for n1 in nums1:
            for n2 in nums2:
                if n1 + n2 in nums1and2:
                    nums1and2[n1+n2] += 1
                else:
                    nums1and2[n1+n2] = 1
        for n3 in nums3:
            for n4 in nums4:
                if -n3 - n4 in nums1and2:
                    answer += nums1and2[-n3-n4]
        return answer
