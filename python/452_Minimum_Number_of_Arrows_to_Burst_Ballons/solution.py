class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points=sorted(points,key = lambda x: x[1])
        answer, end = 0, points[0][1]
        for p in points:
            if p[0] > end:
                answer += 1
                end = p[1]
        return answer + 1
