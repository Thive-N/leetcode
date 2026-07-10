# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeftHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def findRightHeight(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height

    def countNodes(self, root):
        if not root:
            return 0

        lh = self.findLeftHeight(root)
        rh = self.findRightHeight(root)

        # If it's a perfect binary tree
        if lh == rh:
            return (1 << lh) - 1  # 2^lh - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)