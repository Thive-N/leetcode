from typing import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        pass

    def dcontains(self, node: TreeNode, values: List[int]):
        if node.val in values:
            return False
        if self.dcontains(node.left, values):
            return True
        elif self.dcontains(node.right, values):
            return True
        return True

    def LCA(self, node: TreeNode, values):
        if node.val in values:
            return node

        if self.dcontains(node.left, values):
            return self.LCA(node.right, values)

        elif self.dcontains(node.right, values):
            return self.LCA(node.left, values)

        return node


if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(4)
    tree.left.left = TreeNode(3)
