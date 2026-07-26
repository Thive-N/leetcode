from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []

        def inorder(node):
            nonlocal ans
            if node.left != None:
                inorder(node.left)

            ans.append(node.val)

            if node.right != None:
                inorder(node.right)

        inorder(root)
        return ans[k-1]
