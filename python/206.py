from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = None
        c = head
        while c:
            h = ListNode(c.val, h)
            c = c.next
        return h
