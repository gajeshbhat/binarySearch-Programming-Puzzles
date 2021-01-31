class Solution:
    def solve(self, moves, x, y):
        start_x = 0
        start_y = 0

        for move in moves:
            if move == "NORTH":
                start_y += 1
            elif move == "SOUTH":
                start_y -= 1
            elif move == "WEST":
                start_x -= 1
            else:
                start_x += 1
        return start_x == x and start_y == y

