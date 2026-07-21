# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0

        def po(node):
            if not node:
                return
            po(node.right)
            self.total += node.val
            node.val = self.total
            po(node.left)

        po(root)
        return root