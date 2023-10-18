from typing import List
from collections import defaultdict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # building adjacency dict
        adj = defaultdict(list)
        for source, destination in relations:
            adj[source].append(destination)

        cache = defaultdict()

        def dfs(src):
            if src in cache:
                return cache[src]

            res = time[src-1]
            for n in adj[src]:
                res = max(res, time[src - 1] + dfs(n))
            cache[src] = res
            return res

        for i in range(1, n+1):
            dfs(i)

        return max(cache.values())
