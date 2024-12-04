class Solution:
    def convert(self, s: str, numRows: int) -> str:
        grid = []
        for x in range(numRows):
            grid.append([])
        down = True
        cg = 0
        for ch in s:
            grid[cg].append(ch)
            if numRows != 1:
                if down:
                    if cg == numRows - 1:
                        down = False
                else:
                    if cg == 0:
                        down = True
                cg += 1 if down else -1

        s = ""
        for x in grid:
            s = s + "".join(x)

        return s


if __name__ == "__main__":
    s = Solution()
    s.convert("PAYPALISHIRING", 3)
