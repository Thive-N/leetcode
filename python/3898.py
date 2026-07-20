class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        degrees = [0] * n
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 1:
                    degrees[i] += 1
        return degrees