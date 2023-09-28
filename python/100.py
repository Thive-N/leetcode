class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSameTree(self, p, q):
        self.a = p
        self.b = q
        return self.check(self.a, self.b)

    def check(self, a, b):
        if a is None and b is None:
            return True

        elif a is None and b is not None:
            return False

        elif a is not None and b is None:
            return False

        elif a.val != b.val:
            return False
        else:
            return self.check(a.left, b.left) and self.check(a.right, b.right)
