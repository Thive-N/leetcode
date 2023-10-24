class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        vals = []
        def postorder(node):
            if node.left != None:
                postorder(node.left)

            vals.append(node.val)

            if node.right != None:
                postorder(node.right)
        
        postorder(root)
        x = None
        print(vals)
        while vals:
            x = TreeNode(vals.pop(-1), right=x)
        return x
