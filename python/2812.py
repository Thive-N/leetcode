from collections import deque
import heapq
from typing import List

class Solution:
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        # Copy grid
        A = [row[:] for row in grid]

        q = deque()
        for i in range(n):
            for j in range(n):
                if A[i][j] == 1:
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            v = A[i][j]

            for dx, dy in self.dirs:
                x, y = i + dx, j + dy

                if 0 <= x < n and 0 <= y < n and A[x][y] == 0:
                    A[x][y] = v + 1
                    q.append((x, y))

        # Max heap
        pq = [(-A[0][0], 0, 0)]

        while pq:
            neg_sf, i, j = heapq.heappop(pq)
            sf = -neg_sf

            if i == n - 1 and j == n - 1:
                return sf - 1

            for dx, dy in self.dirs:
                x, y = i + dx, j + dy

                if 0 <= x < n and 0 <= y < n and A[x][y] > 0:
                    heapq.heappush(pq, (-min(sf, A[x][y]), x, y))
                    A[x][y] *= -1 

        return A[n - 1][n - 1] - 1