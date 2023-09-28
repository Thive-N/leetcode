# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        return self.check(root, 0)

    def check(self, root, depth):
        if root is None:
            return depth
        else:
            return max(self.check(root.left, depth + 1), self.check(root.right, depth + 1))
