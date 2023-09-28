# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        return self.check(nums, 0, len(nums) - 1)

    def check(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        node.left = self.check(nums, left, mid - 1)
        node.right = self.check(nums, mid + 1, right)
        return node
