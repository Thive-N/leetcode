
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root: Optional[TreeNode], val: int) -> None:
            nonlocal ans
            if not root:
                return
            val = (val << 1) + root.val
            if not root.left and not root.right:
                ans += val
            dfs(root.left, val)
            dfs(root.right, val)

        dfs(root, 0)
        return ans
