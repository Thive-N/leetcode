from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"({self.val})" if self.next is None else f"ListNode({self.val}, {self.next})"


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(4)
    l3 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l4 = ListNode(1)
    l5 = ListNode(3)
    l6 = ListNode(4)
    l4.next = l5
    l5.next = l6
    l7 = ListNode(2)
    l8 = ListNode(6)
    l7.next = l8
    print(s.mergeKLists([l1, l4, l7]))
