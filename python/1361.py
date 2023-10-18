from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = set(leftChild + rightChild)
        parents.discard(-1)
        if len(parents) == n:
            return False

        v = set()
        root = -1

        for i in range(n):
            if i not in parents:
                root = i
                break

        def dfs(i):
            if i == -1:
                return True
            if i in v:
                return False
            v.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])

        return dfs(root) and len(v) == n
