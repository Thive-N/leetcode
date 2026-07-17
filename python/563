# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root):
      self.ans = 0
      self.s(root)
      return self.ans
    
    def s(self, node):
        if not node: return 0
        left, right = self.s(node.left), self.s(node.right)
        self.ans += abs(left - right)
        return node.val + left + right