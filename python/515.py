from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        c = defaultdict(list)
        def bfs(node, depth):
            if node == None:
                return
            c[depth].append(node.val)
            bfs(node.left, depth+1)
            bfs(node.right, depth+1)
        bfs(root,0)
        print(c)
        return [max(v) for k,v in c.items()]

