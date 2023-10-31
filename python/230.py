from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def postorder(node):
            nonlocal ans
            if node.left != None:
                postorder(node.left)

            ans.append(node.val)

            if node.right != None:
                postorder(node.right)

        postorder(root)
        return ans[k-1]
