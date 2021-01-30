class Solution:

    def update_moves(self, move, x, y):
        if move == "NORTH":
            y += 1
        elif move == "SOUTH":
            y -= 1
        elif move == "EAST":
            x += 1
        elif move == "WEST":
            x -= 1
        return (x, y)

    # Time -> O(n) space O(1)
    def solve(self, moves, x, y):
        startX = 0
        startY = 0
        # Store x,y
        move_dict = {}
        for move in moves:
            move_dict[(startX, startY)] = move
            startX, startY = self.update_moves(move, startX, startY)
            while (startX, startY) in move_dict:
                startX, startY = self.update_moves(move, startX, startY)
        # Compare and return results
        if startX == x and startY == y:
            return True
        return False