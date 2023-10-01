from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)

    def traverse(self, root):
        if root == None:
            return 0

        if self.isLeaf(root.left):
            return self.traverse(root.right) + root.left.val

        return self.traverse(root.left) + self.traverse(root.right)

    def isLeaf(self, root):
        if root == None:
            return False
        return root.left == None and root.right == None
