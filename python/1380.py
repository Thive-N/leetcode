from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        minrow = [min(row) for row in matrix]
        maxcol = [max(col) for col in zip(*matrix)]

        return [cell for row in matrix for cell in row if cell in minrow and cell in maxcol]


if __name__ == "__main__":
    s = Solution()
    print(s.luckyNumbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))  # [15]
