from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root == None:
            return 0
        q = [root]
        a = []
        while q:
            e = q.pop(0)
            a.append(e.val)
            if e.left != None:
                q.append(e.left)
            if e.right != None:
                q.append(e.right)

        return sum(filter(lambda x: high >= x >= low, a))
