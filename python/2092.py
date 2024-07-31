from typing import List
import heapq


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj = {}
        adj_set = {}
        for i, j, t in meetings:
            if t not in adj:
                adj[t] = []
            if t not in adj_set:
                adj_set[t] = set()

            adj_set[t].add(i)
            adj_set[t].add(j)
            adj[t].append((i, j))

        q = set([0, firstPerson])

        for t in sorted(adj.keys()):
            if len(q.union(adj_set[t])) > 0:
                for _ in range(2):
                    for i, j in adj[t]:
                        if i in q or j in q:
                            q.add(i)
                            q.add(j)

        return list(q)


if __name__ == "__main__":
    s = Solution()
    print(s.findAllPeople(4, [[3, 1, 3], [1, 2, 2], [0, 3, 3]], 3))
