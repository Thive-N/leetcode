from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(n):
            if not n:
                return
            if not n.left and not n.right:
                yield n.val
            else:
                yield from dfs(n.left)
                yield from dfs(n.right)
        return list(dfs(root1)) == list(dfs(root2))
