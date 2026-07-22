class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        # 0 = right, 1 = down, 2 = left, 3 = up
        d = 0

        while True:
            if d == 0:
                spiral += matrix[0]
                matrix = matrix[1:]
            elif d == 1:
                for row in matrix:
                    spiral.append(row[-1])
                    row.pop()
            elif d == 2:
                spiral += matrix[-1][::-1]
                matrix = matrix[:-1]
            elif d == 3:
                for row in matrix[::-1]:
                    spiral.append(row[0])
                    row.pop(0)

            if not matrix or not matrix[0]:
                break

            d = (d + 1) % 4
        return spiral