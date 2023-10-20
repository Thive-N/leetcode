class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = y = 0
        for x in moves:
            if x == "U":
                y += 1
            if x == "D":
                y -= 1
            if x == "L":
                x -= 1
            if x == "R":
                x += 1
        return x == 0 and y == 0
