class Solution:
    def reverseSubmatrix(self, grid: list[list[int]], start_row: int, start_col: int, size: int) -> list[list[int]]:
        end_col = start_col + size - 1

        for col in range(start_col, end_col + 1):
            for offset in range(size // 2):
                top_row = start_row + offset
                bottom_row = start_row + size - offset - 1

                grid[top_row][col], grid[bottom_row][col] = (
                    grid[bottom_row][col],
                    grid[top_row][col],
                )

        return grid