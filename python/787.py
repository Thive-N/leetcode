from typing import List
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Create adjacency list
        d = {i: [] for i in range(n)}
        for u, v, w in flights:
            d[u].append((v, w))

        # Priority queue (price, city, stops)
        q = [(0, src, 0)]

        # Dictionary to track minimum cost to reach each city with a given number of stops
        costs = {(src, 0): 0}

        while q:
            price, city, stops = heapq.heappop(q)

            if city == dst:
                return price

            if stops > k:
                continue

            for neighbor, cost in d[city]:
                new_cost = price + cost
                if new_cost < costs.get((neighbor, stops + 1), float('inf')):
                    costs[(neighbor, stops + 1)] = new_cost
                    heapq.heappush(q, (new_cost, neighbor, stops + 1))

        return -1


if __name__ == "__main__":
    print(Solution().findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1))  # 200
