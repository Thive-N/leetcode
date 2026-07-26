from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, parent_val=0):
            if node == None:
                print(f"Node Value")
                return 0

            val = (parent_val*10) + node.val

            if not node.left and node.right:
                return parent_val
            
            l = dfs(node.left,val)
            r = dfs(node.right,val)
            return l+r
        return dfs(root)


if __name__ == "__main__":
    s = Solution()
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    print(s.sumNumbers(tree))  # Output: 25