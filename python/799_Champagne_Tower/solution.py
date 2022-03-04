class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * (r+1) for r in range(query_row + 1)]
        tower[0][0] = poured
        for row in range(len(tower)):
            for g, vol in enumerate(tower[row]):
                if vol > 1:
                    if row != len(tower) - 1:
                        excess = (vol - 1) / 2
                        tower[row+1][g] += excess
                        tower[row+1][g+1] += excess
                    tower[row][g] = 1
        return tower[query_row][query_glass]
