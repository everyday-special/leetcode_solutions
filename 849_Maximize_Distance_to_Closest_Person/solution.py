class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        biggest_gap, curr_gap, factor = 0, 0, 2
        for i in range(len(seats)):
            if not seats[i]:
                if i == 0 or i == len(seats) - 1:
                    factor = 1
                curr_gap += 1
            else:
                biggest_gap = max(biggest_gap, curr_gap // factor + curr_gap % factor)
                factor, curr_gap = 2, 0
        return max(biggest_gap, curr_gap)
