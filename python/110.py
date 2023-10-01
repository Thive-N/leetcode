# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return True if self.checkBalance(root) != -1 else False

    def checkBalance(self, root):
        if root is None:
            return 0

        lh = self.checkBalance(root.left)
        rh = self.checkBalance(root.right)

        if lh == -1 or rh == -1:
            return -1

        if abs(lh - rh) > 1:
            return -1

        return max(lh, rh) + 1
