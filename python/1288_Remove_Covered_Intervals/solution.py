# Slow O(N ** 2) solution

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        answer = 0
        for i in range(len(intervals)):
            overlap = False
            for j in range(len(intervals)):
                if i == j:
                    continue
                if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                    overlap = True
            if not overlap:
                answer += 1
        return answer
