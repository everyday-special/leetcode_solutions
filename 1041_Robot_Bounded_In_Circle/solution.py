class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos_vector, direction = [0, 0], 'N' # Initialize robot position and direction
        change_direction = {'N':('W', 'E'), 'W': ('S', 'N'), 'S':('E', 'W'), 'E':('N', 'S')} # Map directional change based on current direction
        change_position = {'N': (0, 1), 'W': (-1, 0), 'S':(0, -1), 'E':(1, 0)} # Map position change based on current direction
        turn = {'L':0, 'R':1} # Map L and R to indexes
        for ch in instructions:
            if ch == 'G':
                pos_vector[0] += change_position[direction][0]
                pos_vector[1] += change_position[direction][1]
            else:
                direction = change_direction[direction][turn[ch]]
        if pos_vector == [0, 0] or direction != 'N':
            return True
        return False
