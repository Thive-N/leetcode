from typing import Optional, List
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def postorder(node):
            nonlocal ans
            if node.left != None:
                postorder(node.left)

            ans.append(node.val)

            if node.right != None:
                postorder(node.right)

        postorder(root)
        c = Counter(ans)

        m = c.most_common()[0][1]
        return [x for x, i in c.items() if i == m]
