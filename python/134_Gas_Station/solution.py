class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank, start = 0, 0
        for i, g in enumerate(gas):
            tank += g - cost[i]
            if tank < 0:
                start, tank = i + 1, 0
        return start
