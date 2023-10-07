from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        o = []
        s = []
        curr = head
        while curr:
            if curr.val in o:
                curr = curr.next
                continue
            if curr.val in s:
                o.append(curr.val)
                s.remove(curr.val)
                curr = curr.next
                continue
            s.append(curr.val)
            curr = curr.next

        new = None
        for x in s[::-1]:
            temp = ListNode(x, new)
            new = temp

        return new
