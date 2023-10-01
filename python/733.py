from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        q.append([sr, sc])
        tf = image[sr][sc]
        rm = len(image)
        cm = len(image[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        filled = [[sr, sc]]
        while q:
            exp = q.popleft()
            if image[exp[0]][exp[1]] != tf:
                continue
            image[exp[0]][exp[1]] = color

            for x, y in directions:
                if exp[0] + x >= rm or exp[0] + x < 0 or exp[1] + y >= cm or exp[1] + y < 0:
                    continue
                tofill = [exp[0]+x, exp[1]+y]
                if tofill in filled:
                    continue

                q.append(tofill)
                filled.append(tofill)
        return image


s = Solution()
print(s.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 0))
