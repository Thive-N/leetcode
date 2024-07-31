from typing import *
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        h = {}
        children = set()

        for p, c, l in descriptions:
            children.add(c)
            if p not in h:
                h[p] = TreeNode(p)
            if c not in h:
                h[c] = TreeNode(c)

            if l:
                h[p].left = h[c]
            else:
                h[p].right = h[c]

        for p, c, l in descriptions:
            if p not in children:
                return h[p]


if __name__ == "__main__":
    s = Solution()
    s.createBinaryTree(d)
