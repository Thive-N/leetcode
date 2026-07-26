# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node: return True

            if node.val <= lower or node.val >= upper:
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root)