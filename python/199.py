# Definition for a binary tree node.
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res


        q = deque()
        q.append(root)

        while q:
            r = None
            level_len = len(q)

            for x in range(level_len):
                node = q.popleft()
                if node:
                    r = node
                    q.append(node.left)
                    q.append(node.right)

            if not r:
                break
            res.append(r.val)