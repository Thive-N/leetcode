from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append([root, 1])

        while queue:
            expand = queue.popleft()
            if expand[0] == None:
                continue
            if expand[0].left == None and expand[0].right == None:
                return expand[1]

            queue.append([expand[0].left, expand[1] + 1])
            queue.append([expand[0].right, expand[1] + 1])

        return 0
