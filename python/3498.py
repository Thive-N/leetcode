class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        while s != "1":
            if int(s, 2) % 2 == 0:
                s = bin(int(s, 2) // 2)[2:]
            else:
                s = bin(int(s, 2) - 1)[2:]
            degree += 1
        return degree