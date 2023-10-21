class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = 0
        c = head
        while c:
            n = n*2 + c.val
            c = c.next
        return n
